# Prior art — hybrid knowledge-graph + vector retrieval

**Research question:** What is the prior art for combining knowledge-graph traversal with vector similarity search in one retrieval system, and how does Swanson-style ABC/LBD discovery map onto graph queries over the estate's AGE + pgvector spine?

**Type:** Prior-art / "shoulders of giants" survey. Internet research pass.
**Relates to:** the canonical PostgreSQL + Apache AGE (graph) + pgvector/HNSW (vector) spine; `amplified-knowledge-mcp` `query_graph`/`search_knowledge`; `pudding-core`'s "Four Russian Stack".

---

## What was already known (existing estate prior art — do not re-litigate)

- Knowledge note *"Canonical Data Architecture"* (Devon-973e, 2026-05-08): the stack is **PostgreSQL + Apache AGE + pgvector (HNSW)**, one engine, three capabilities; FalkorDB/Qdrant deprecated (AMP-344). "The Russian maths" is explicitly defined there as **HNSW by Malkov & Yashunin (2016)**.
- `clean-build/01_truth/schemas/2026-03_pudding-code-specification_v1.md` and `..._taxonomy-synthesis_v1.md` already cite **Swanson (1986)**, **Jaccard (1901)**, **Church & Hanks (1990, PMI)**, **ICD-10 (WHO, 1990)**. Those foundations are taken as given here.
- APDS knowledge note: dual-path matching = **Jaccard + PMI (deterministic)** in parallel with **Claude (semantic)**; emergence score `E = (B × D × N) / R`.

**What is new in this file:** the specific *hybrid retrieval* literature (GraphRAG, RRF) that sits **between** the graph layer and the vector layer, plus the primary HNSW/AGE/pgvector sources, and an explicit mapping of Swanson's ABC model onto an openCypher query pattern.

---

## Key findings (with citations)

### 1. GraphRAG (Microsoft) — the canonical graph+LLM retrieval design
- "We propose a Graph RAG approach… uses an LLM to build a graph-based text index in two stages: first to derive an entity knowledge graph from the source documents, then to pre-generate community summaries for all groups of closely-related entities." Source: Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization," arXiv:2404.16130 (2024) — https://arxiv.org/abs/2404.16130 / PDF https://r.jordan.im/download/language-models/2404.16130v1.pdf (confidence: high, primary paper, Microsoft Research).
- Two retrieval modes, both relevant to the estate:
  - **Local search** — "combines structured data from the knowledge graph with unstructured data from the input documents to augment the LLM context with relevant entity information at query time." https://microsoft.github.io/graphrag/query/local_search/
  - **Global search** — map-reduce over LLM-generated **community reports** to answer whole-corpus "what are the themes?" questions. https://github.com/microsoft/graphrag/blob/main/docs/query/global_search.md
- Framing quote worth keeping: sensemaking is "a motivated, continuous effort to understand connections… in order to anticipate their trajectories and act effectively" (Klein et al. 2006, quoted in the paper). This is precisely the Pudding Technique's premise stated in the RAG literature. (confidence: high.)

### 2. Hybrid retrieval via Reciprocal Rank Fusion (RRF) — merge graph/keyword/vector rankings
- RRF "aggregates rankings from multiple searches… into a single ranking that is more accurate," parameter-free, unsupervised, no score calibration needed. Sources: MongoDB, "Better RAG Results With Reciprocal Rank Fusion," 2026-01-12 — https://www.mongodb.com/resources/basics/reciprocal-rank-fusion; Elastic Search Labs, "Hybrid retrieval," 2023-07-20 — https://www.elastic.co/search-labs/blog/improving-information-retrieval-elastic-stack-hybrid (confidence: high, vendor-primary but the RRF formula is standard).
- Rationale for hybridising: "lexical retrievers (such as BM25) and semantic retrievers… are somewhat complementary" — combining them improves relevance because relevant docs match across methods more often than irrelevant ones (Elastic, same source). The same complementarity argument extends to **graph-traversal recall + vector-similarity recall**.
- Note: the estate's MCP server already has `search_knowledge` (vector) and `query_graph` (Cypher) as *separate* tools. RRF is the prior art for a **third tool that fuses them** — this is genuinely new capability, not a re-implementation.

### 3. HNSW — the "Russian maths" primary source
- Malkov & Yashunin, "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs," arXiv:1603.09320 (2016), later IEEE TPAMI 2018 (DOI 10.1109/TPAMI.2018.2889473). Multi-layer proximity graphs; upper-layer entry + scale separation give **logarithmic complexity scaling**; heuristic neighbour selection boosts recall on clustered data. Sources: https://arxiv.org/abs/1603.09320 ; https://doi.org/10.1109/tpami.2018.2889473 (confidence: high, primary). This is the exact algorithm the canonical-data knowledge note names "the Russian maths."

### 4. pgvector — vectors co-located with relational data
- pgvector adds a `vector` type to Postgres 13+, supports exact and approximate NN, L2 / inner product / cosine / L1 / Hamming / **Jaccard** distances, and IVFFlat + HNSW indexes. Source: https://github.com/pgvector/pgvector ; https://pgxn.org/dist/vector (confidence: high, primary repo). Key architectural point (Google Cloud restatement): "store, search, and index them directly in your relational database… without having to move data around" — https://cloud.google.com/discover/what-is-pgvector. **Note for the estate:** pgvector natively supports Jaccard distance on binary vectors — a possible deterministic-path accelerator for the Pudding Jaccard-slot scoring.

### 5. Apache AGE — openCypher graph inside the same Postgres
- "Apache AGE is an extension for PostgreSQL that enables users to leverage a graph database on top of the existing relational databases… use the standard ANSI SQL along with openCypher." Supports hybrid SQL+Cypher querying and multiple graphs. Sources: https://age.apache.org/ ; https://github.com/apache/age ; https://age.apache.org/age-manual/master/intro/overview.html (confidence: high, primary). This is what makes graph traversal and vector search share **one transaction and one engine** — the structural precondition for cheap hybrid retrieval.

### 6. Swanson ABC/LBD mapped onto a graph query
- Swanson's model: `A→B` known in one literature, `B→C` known in another, `∴ A→C` undiscovered (already cited in-estate). In graph terms this is an **open-triad / 2-hop path-completion query**: find nodes `A` and `C` connected via a shared `B` but with **no direct `A–C` edge**. In openCypher over AGE this is expressible directly:
  ```cypher
  MATCH (a:Concept)-[:BRIDGES]->(b:Concept)-[:BRIDGES]->(c:Concept)
  WHERE a <> c AND NOT (a)-[:BRIDGES]-(c)
  RETURN a, b, c
  ```
  (Node/edge labels `Concept`/`BRIDGES` match the APDS schema in the estate knowledge note.) The graph layer *finds candidate ABC triads*; the vector layer *scores domain distance / novelty* via embeddings; RRF or the APDS `E` score *ranks* them. This is the hybrid design's payoff: LBD is a graph-shaped problem, scoring is a vector-shaped problem, and AGE+pgvector lets both run in one place. (confidence: this mapping is OPINION, 85% — the openCypher pattern is standard, but whether the live graph uses exactly these labels needs verification against `pudding-core`.)

---

## How it maps to the estate

| Prior-art element | Estate component | Mapping |
|---|---|---|
| GraphRAG local search | `amplified-knowledge-mcp` `query_graph` + `search_knowledge` | The two halves already exist as separate tools; GraphRAG is the reference design for fusing them at query time. |
| GraphRAG global/community summaries | PUDDING recipe graphs / cross-vertical pattern reports | Community-report pre-summarisation is prior art for the APDS "cross-vertical pattern report" output stream. |
| RRF | (not yet built) | New capability: a fused-retrieval MCP tool merging graph + vector rankings. |
| HNSW (Malkov & Yashunin 2016) | pgvector HNSW index / "Four Russian Stack" | The named "Russian maths." Verify whether `pudding-core`'s "Four Russian Stack" refers to HNSW + other Soviet-origin algorithms (e.g. Method of Four Russians for boolean matrix mult) — attribution chain must stay honest (see next action). |
| pgvector Jaccard distance | Pudding Jaccard-slot scoring (deterministic path) | Possible native accelerator for the Jaccard confidence band. |
| AGE openCypher | Graph layer of the spine | Enables the 2-hop ABC path-completion query in-engine. |
| Swanson ABC (1986) | Pudding Technique / APDS Match stage | LBD = open-triad graph query; already-cited foundation, now given an explicit query form. |

---

## Confidence band

- GraphRAG / RRF / HNSW / pgvector / AGE as correct, citable prior art: **high (90–95%)** — all primary sources.
- ABC-as-openCypher-path-completion mapping: **OPINION 85%** (standard graph pattern; live label names need checking against `pudding-core`).
- pgvector native Jaccard as a deterministic-path accelerator: **OPINION 70%** (plausible, unverified against the actual scoring code).

## Recommended next action (for Devon to assess; NOT auto-promoted)

1. **Attribution honesty check (do first):** confirm exactly what `pudding-core`'s **"Four Russian Stack"** names. If it includes the *Method of Four Russians* (Arlazarov, Dinic, Kronrod, Faradzhev, 1970) distinct from HNSW, both attributions must be recorded separately — do not collapse them. File as a Knowledge note correction if the current note conflates them.
2. Propose (Linear, Knowledge spine) a **fused-retrieval MCP tool** using RRF over `query_graph` + `search_knowledge`, citing GraphRAG local search as the reference design.
3. Prototype the **2-hop ABC path-completion Cypher** against the live AGE graph to validate the LBD-as-graph-query mapping before promoting it to `clean-build`.

---

*Devon | 2026-07-08 | session devin-8aa5624849524edaa4556b176bf0df69*
*Research question: prior art for hybrid knowledge-graph + vector retrieval (GraphRAG, RRF, HNSW, pgvector, Apache AGE) and how Swanson ABC/LBD maps onto graph queries over the estate's AGE+pgvector spine.*
