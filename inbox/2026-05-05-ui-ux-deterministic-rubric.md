# UI/UX Deterministic Rubric + Component System
## For AI-Generated Agent-Facing Dashboards at Amplified Partners

**Date:** 2026-05-05  
**Audience:** Cassian + architect → routing to Hermes/Devon for component-system implementation  
**Scope:** The 90% locked layer ABOVE the existing visual-polish-system scoring engine. Not a rewrite of the scoring engine. Not a new JS stack.

---

## 1. Codifiable Rules from Primary Sources

### 1.1 Refactoring UI (Wathan & Schoger)

Source: [Refactoring UI notes — maibuith.com](https://maibuith.com/notes/refactoring-ui) and [Updivision review](https://updivision.com/blog/post/book-review-refactoring-ui-by-adam-wathan-steve-schoger)

**Spacing and sizing system — verbatim:**

> "A linear scale won't work: A useful system considers the *relative* difference between adjacent values. Eg. 12px vs 16px is a big difference, but 500px vs 520px won't make a big difference. Make sure no two values in your scale are ever closer than about 25%."

> "Start with a sensible base value, then build a scale using factors and multiples of that value. 16px is great to start with because it divides nicely and is the default font size in major web browsers."

**Typography scale — verbatim:**

> "A linear scale won't work: Smaller jumps at bigger font sizes make you waste time deciding, eg. between 46px and 48px."

> "Modular scales using ratio like 4:5, 2:3, or golden ratio: May create fractional values like 31.25px, 48.828px and browsers handle pixel rounding differently → round the values if you want to use this approach."

> "The authors recommend a scale of 11 font sizes, with smaller jumps between sizes at the bottom of the scale (2px) and increasingly larger jumps between sizes as you go up (up to 12px). Again, size is relative."

**Line height — verbatim:**

> "Line-height and paragraph width should be proportional — narrow content can use a shorter line-height like 1.5, but wide content might need a line-height as tall as 2. Tight line height might make readers go back to the left edge unsure which line is next."

**Ambiguous spacing — verbatim:**

> "Whenever you're relying on spacing to connect a group of elements, always make sure there's more space around the group than there is within it."

**Systematize everything** — the book enumerates these properties as needing a locked system: font size, font weight, line height, color, margin, padding, width, height, box shadows, border radius, border width, opacity.

---

### 1.2 Material Design 3 Type Scale

Source: [Material Design 3 Typography Overview](https://m3.material.io/styles/typography/overview)

Material Design 3 defines **30 type styles** (15 baseline + 15 emphasized), organised into five semantic roles:

| Role | Sizes | Purpose |
|------|-------|---------|
| Display | Large / Medium / Small | Largest text, short important strings |
| Headline | Large / Medium / Small | High-emphasis short text |
| Title | Large / Medium / Small | Medium-emphasis shorter text |
| Body | Large / Medium / Small | Long-form, readable prose |
| Label | Large / Medium / Small | Small utility text, labels, captions |

> "Use Material tokens to easily define font, line height, size, tracking, weight, and more."

> "The M3 type scale has 30 type styles: 15 baseline and 15 emphasized."

From the UX Collective semantic tokens article ([source](https://uxdesign.cc/mastering-typography-in-design-systems-with-semantic-tokens-and-responsive-scaling-6ccd598d9f21)):

> "In our typography system, we use a **smart ratio-based approach** to determine line height. Depending on the type scale, we adjust the ratio: a tighter 1.14 ratio works well for larger text like displays and prominent headings, while a 1.5 ratio is ideal for smaller text like body copy and captions. Once calculated, these line heights are rounded to the nearest 4px."

> "For a large heading with a 48px font at a 1.14 ratio, the line height comes out to roughly 56px. For body text with a 16px font using a 1.5 ratio, the line height is 24px."

---

### 1.3 Apple Human Interface Guidelines — 8-Point Grid

Source: [Apple HIG Figma implementation](https://gist.github.com/eonist/e79ca41b312362682343c41f63062734)

> "Apply Figma's Layout Grids with 8pt increments to create consistent negative space."

The 8-point grid spacing scale: `spacing.xxs: 4pt`, `spacing.xs: 8pt`, `spacing.s: 12pt`, `spacing.m: 16pt`, `spacing.l: 24pt`, `spacing.xl: 32pt`, `spacing.xxl: 48pt`.

**Component minimum heights:** standard cell 44pt, subtitle cell 60pt — the 44pt minimum touch target is the hard floor for interactive elements.

**Container padding:** Standard screen edge margin 16pt (small screens) / 20pt (large screens). Card internal padding: 16pt all sides. Section containers: 16pt top/bottom, 16pt left/right.

---

### 1.4 Nielsen's 10 Usability Heuristics

Source: [Nielsen Norman Group — 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)

Verbatim:

1. **Visibility of System Status** — "The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time."

2. **Match Between the System and the Real World** — "The design should speak the users' language. Use words, phrases, and concepts familiar to the user, rather than internal jargon. Follow real-world conventions, making information appear in a natural and logical order."

3. **User Control and Freedom** — "Users often perform actions by mistake. They need a clearly marked 'emergency exit' to leave the unwanted action without having to go through an extended process."

4. **Consistency and Standards** — "Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform and industry conventions."

5. **Error Prevention** — "Good error messages are important, but the best designs carefully prevent problems from occurring in the first place. Either eliminate error-prone conditions, or check for them and present users with a confirmation option before they commit to the action."

6. **Recognition Rather than Recall** — "Minimize the user's memory load by making elements, actions, and options visible. The user should not have to remember information from one part of the interface to another. Information required to use the design (e.g. field labels or menu items) should be visible or easily retrievable when needed."

7. **Flexibility and Efficiency of Use** — "Shortcuts — hidden from novice users — may speed up the interaction for the expert user so that the design can cater to both inexperienced and experienced users. Allow users to tailor frequent actions."

8. **Aesthetic and Minimalist Design** — "Interfaces should not contain information that is irrelevant or rarely needed. Every extra unit of information in an interface competes with the relevant units of information and diminishes their relative visibility."

9. **Help Users Recognize, Diagnose, and Recover from Errors** — "Error messages should be expressed in plain language (no error codes), precisely indicate the problem, and constructively suggest a solution."

10. **Help and Documentation** — "It's best if the system doesn't need any additional explanation. However, it may be necessary to provide documentation to help users understand how to complete their tasks."

Heuristics #4 (Consistency), #6 (Recognition over Recall), and #8 (Minimalist Design) are the three most directly codifiable into a deterministic rubric for agent-facing dashboards.

---

## 2. Cognitive Load Theory Applied to Dashboards

### 2.1 Sweller's Three Load Types

Source: [NNGroup — Minimize Cognitive Load to Maximize Usability](https://www.nngroup.com/articles/minimize-cognitive-load/)

> "**Intrinsic cognitive load** is the effort of absorbing that new information and of keeping track of their own goals."

> "Designers should, however, strive to eliminate, or at least minimize, **extraneous cognitive load**: processing that takes up mental resources, but doesn't actually help users understand the content (for example, different font styles that don't convey any unique meaning)."

> "Many of our top usability guidelines — from chunking content to optimizing response times — are aimed at minimizing cognitive load."

**Germane load** supports schema-building — the productive load that leads to comprehension.

### 2.2 Dashboard-Specific Findings

Source: [IJRTI — Interactive Dashboarding Techniques to Minimize Cognitive Load](https://www.ijrti.org/papers/IJRTI2510085.pdf)

> "Based on the cognitive load theory, the paper explores the ability of progressive disclosure, adaptive filtering, dynamic visual hierarchies, contextual drill-through, and responsive feedback to work in harmony to increase the usability of dashboards."

> "The main role of interactive dashboarding techniques is to decrease extraneous load and maximize germane one so that users can apply their mental resources to meaningful information."

Five techniques that reduce extraneous load in BI dashboards (table from source):

| Technique | Cognitive Load Addressed | Primary Benefit |
|-----------|--------------------------|-----------------|
| Progressive Disclosure | Reduces extraneous by withholding non-essential details | Users focus on key insights first |
| Interactive Filtering | Minimizes intrinsic by narrowing datasets | Focused analysis |
| Dynamic Visual Hierarchies | Reduces extraneous + intrinsic by directing attention | Speeds identification of priorities |
| Adaptive Interfaces | Minimizes extraneous for novices | Aligns complexity with user expertise |
| Contextual Drill-Through | Reduces extraneous by consolidating related data | Simplifies navigation |

From Taylor & Francis, real-time operational dashboard research ([source](https://www.tandfonline.com/doi/full/10.1080/12460125.2025.2593245)):

> "We find that task-related cognitive demand depends on the kind of displayed information. However, prescriptions added to predictions break frustration as an emotional response since participants rely on the system."

> "While with predictive dashboards, users are somewhat relieved from the task of extrapolating information themselves to generate decision alternatives. They now must recognise and assess predictions that are presented to them in addition to descriptive information."

**Key implication for agent-facing dashboards:** showing *what the system is doing* (prescriptive/status) reduces frustration more than showing only raw data. Agents like Hermes and Mirror need system-state legibility, not aesthetic flair.

Source: [NNGroup cognitive load](https://www.nngroup.com/articles/minimize-cognitive-load/):

> "1. **Avoid visual clutter**: redundant links, irrelevant images, and meaningless typography flourishes slow users down."  
> "2. **Build on existing mental models**: When you use labels and layouts that they've encountered on other websites, you reduce the amount of learning they need to do on your site."  
> "3. **Offload tasks**: Look for anything in your design that requires users to read text, remember information, or make a decision. Then look for alternatives: can you show a picture, re-display previously entered information, or set a smart default?"

---

## 3. WCAG 2.2 AA Floor

Source: [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)

### 3.1 Colour Contrast

**SC 1.4.3 Contrast (Minimum) — Level AA:**

> "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for the following:
> - **Large Text** Large-scale text and images of large-scale text have a contrast ratio of at least 3:1;
> - **Incidental** Text or images of text that are part of an inactive user interface component, that are pure decoration, that are not visible to anyone, or that are part of a picture that contains significant other visual content, have no contrast requirement.
> - **Logotypes** Text that is part of a logo or brand name has no contrast requirement."

"Large text" is defined as: 18pt (24px) or larger at any weight; OR 14pt bold (approximately 18.66px bold) or larger.

**SC 1.4.11 Non-text Contrast — Level AA:**

> "The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s):
> - **User Interface Components** Visual information required to identify user interface components and states, except for inactive components or where the appearance of the component is determined by the user agent and not modified by the author;
> - **Graphical Objects** Parts of graphics required to understand the content, except when a particular presentation of graphics is essential to the information being conveyed."

### 3.2 Focus Visibility

**SC 2.4.7 Focus Visible — Level AA:**

Source: [W3C WAI Understanding 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)

> "Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible."

> "The focus indicator must not be time limited, when the keyboard focus is shown it must remain."

**SC 2.4.11 Focus Not Obscured (Minimum) — Level AA (new in WCAG 2.2):** When a UI component receives focus, the component is not entirely hidden due to author-created content.

**SC 2.5.8 Target Size (Minimum) — Level AA (new in WCAG 2.2):** The target size for pointer inputs is at least 24×24 CSS pixels.

### 3.3 Text Spacing

**SC 1.4.12 Text Spacing — Level AA:**

> "In content implemented using markup languages that support the following text style properties, no loss of content or functionality occurs by setting all of the following and by changing no other style property:
> - Line height (line spacing) to at least 1.5 times the font size;
> - Spacing following paragraphs to at least 2 times the font size;
> - Letter spacing (tracking) to at least 0.12 times the font size;
> - Word spacing to at least 0.16 times the font size."

### 3.4 Motion

**SC 2.3.3 Animation from Interactions — Level AAA** (note: AAA, not AA floor):

> "Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed."

Source: [W3C WAI Understanding 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)

> "The intent of this success criterion is to allow users to prevent animation from being displayed on web pages. Some users experience distraction or nausea from animated content."

The sufficient technique: `C39: Using the CSS prefers-reduced-motion query to prevent motion`. The existing visual-polish-system design tokens (50ms–500ms motion range) should be wrapped:

```css
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

**SC 2.2.2 Pause, Stop, Hide — Level A:** Auto-updating content (polling refreshes, live data streams) must be pauseable.

---

## 4. AI-Generated UI Quality Research 2025–2026

### 4.1 What Determines Quality

Source: [Vercel — Maximizing Outputs with v0](https://vercel.com/blog/maximizing-outputs-with-v0-from-ui-generation-to-code-creation)

> "To get the highest quality generations, you need to be able to craft input prompts to guide v0 well. The better you guide v0 and understand its strengths, the more accurate and relevant the responses you'll get."

> "The more details you write, the better v0 can tailor its response to your needs: Include desired functionality of specific components; Specify design preferences for every element; Mention any libraries or frameworks you want to use; Describe the context or use case for the component within the app you're working on."

Source: [UXMagic — AI Design Prompt Templates for SaaS](https://uxmagic.ai/blog/production-ready-ai-design-prompts-saas)

> "If you don't define structure, AI defaults to statistical averages: Dark sidebar. 4 symmetrical KPI cards. Random line chart. Airy spacing. Zero hierarchy. Algorithmic homogenization at its finest."

> "To escape this, your prompt must define: Data Schema (Explicit data types, Character limits, Required columns, Density expectations); Structural Grid Rules (8pt grid, Row heights, Divider rules); Persona & Cognitive Context."

> "If you treat it like a deterministic compiler with strict constraints, data schemas, structural grids, and enforced reasoning, you'll get acceleration. The difference is discipline. Start writing prompts like PRDs."

### 4.2 Context Amnesia and Spec Drift

Source: [r/ClaudeCode — production use](https://www.facebook.com/groups/claudeaicommunity/posts/1225528916280940/)

> "I built an extensive rule system over 22 sessions — plan before code, audit before implementation, verify before declaring done, specific UI standards, specific file handling rules. Claude confirms understanding of every rule. Then ignores them on the very next prompt. Every session. Every time."

This is the central practical argument for the Spine 5 90/10 commitment: you cannot prompt-engineer your way to deterministic UI. The 90% must be locked in code, tokens, and template structure that the LLM cannot deviate from — it only fills the 10% interstices.

### 4.3 Design System as Constraint Layer

Source: [Giuseppe Galati — Design System for AI-Generated UI (LinkedIn)](https://www.linkedin.com/posts/galatigiuseppe_i-built-a-design-system-made-for-vibe-coding-activity-7445489036648996865-mIva)

> "Claude doesn't guess how a button should behave — it knows, because the system tells it... When I vibe code with Claude, it doesn't invent. It builds with my system. Same visual language. Same spacing. Same colors. Same interaction patterns. Every time. This is the shift I believe in: the design system isn't dead — it's the missing layer that makes AI-generated UI actually production-ready."

> "One command. One sentence. Full prototype. You describe what you want in plain English. The CLI sends your app's actual design system — tokens, components, theme config, guidelines — as locked, immutable context to an AI code generator. The AI can't override your design system. It can only build with it."

The iterative zoom-in method for AI UI generation ([DEV Community](https://dev.to/a_shokn/how-to-break-the-ai-generated-ui-curse-your-guide-to-authentic-professional-design-2en)):

> "Initial Draft (50%) → Second Pass (99%) → Micro Pass (99% → 100%). AI tends to falter when you expect it to deliver perfection in a single attempt. However, by layering your instructions — starting with the big picture, then moving to details, and finally to micro details — you enable it to identify mistakes it previously overlooked."

---

## 5. Best LLM for UI Generation — Comparative Evidence

### 5.1 Instruction-Following and Spec Compliance

Source: [DEV Community — Claude Sonnet 4 vs Gemini 2.5 Pro](https://dev.to/composiodev/claude-sonnet-4-vs-gemini-25-pro-coding-comparison-5787)

> "Claude Sonnet 4 is definitely superior to Gemini 2.5 Pro in coding... Claude consistently preserved API stability, avoided breaking changes, and significantly reduced the burden of code reviews."

> "Results showed that Claude Sonnet 4 completed tasks at an impressive speed, outperforming Gemini by a factor of 2.8 (averaging 6 minutes and 5 seconds compared to Gemini's 17 minutes and 1 second). Furthermore, Claude achieved a flawless task completion rate, strictly following the required file modifications. In contrast, Gemini altered extra, unspecified files in 78% of its tasks and inadvertently added features almost half the time."

Source: [r/Bard extended testing](https://www.reddit.com/r/Bard/comments/1kwpzpv/spent_104_testing_claude_sonnet_4_vs_gemini_25/)

> "Claude consistently preserved API stability, avoided breaking changes, and significantly reduced the burden of code reviews."

**Counter-evidence on Gemini for planning:** The same thread notes Gemini 2.5 Pro produces better "design and infrastructure planning documents" with greater quantity and quality. This suggests a split: Claude for code generation with a spec; Gemini for upstream planning/architecture when the spec doesn't yet exist.

### 5.2 v0.dev as Specialist

v0.dev is React/Tailwind/shadcn only — not applicable to the Python-server-rendered substrate. Its prompt patterns are instructive but the platform itself is not in scope.

### 5.3 LLM Leaderboard Context

Source: [Iternal — Definitive LLM Selection Guide](https://iternal.ai/llm-selection-guide)

For code (SWE-bench Verified): Claude Opus 4.6, GPT-5.4, and MiniMax M2.5/M2.7 lead. For instruction-following + spec adherence at reasonable cost, the weight of evidence favours **Claude Sonnet** (current generation) over Gemini 2.5 Pro — because Gemini has a documented tendency to add unsolicited features and alter out-of-scope files.

---

## 6. Server-Side Python UI Stacks

### 6.1 FastAPI + HTMX + Jinja2 (The No-Build Stack)

Source: [Blake Crosley — FastAPI + HTMX: The No-Build Full-Stack](https://blakecrosley.com/guides/fastapi-htmx)

> "FastAPI + HTMX + Alpine.js + Jinja2 + plain CSS produces production web applications with zero build tools, zero `node_modules/`, and perfect Lighthouse scores."

Performance (verified):

| Metric | Value |
|--------|-------|
| Lighthouse Performance | 100 |
| Total JS shipped | 32–46KB |
| First visit payload | 45–60KB |
| Dependencies | 15 Python packages vs 311+ npm |
| Deploy pipeline | `git push` → live in ~40s |
| Build step | None |

> "Server-rendered HTML eliminates: Client state management, JSON serialization boundaries, hydration mismatches."

Decision boundary from the same source:

> "Content sites, CRUD apps, dashboards, portfolios, internal tools, documentation → FastAPI+HTMX (solo/small team)"

**What no-build gives up:** TypeScript, HMR, tree shaking, npm libraries (Radix, shadcn/ui). For a Python shop at 187k LOC, this is not a loss — it is a constraint that keeps the substrate coherent.

### 6.2 Reflex

Source: [Reflex — Python Web Development Frameworks comparison](https://reflex.dev/blog/python-comparison/)

> "Reflex allows you to build both your frontend and backend in Python... When deployed, Reflex apps are transpiled into a FastAPI backend with a React frontend."

Reflex compiles to React. This means a JS build step exists at deploy time, Reflex-generated HTML is React-rendered, and the output is harder to audit directly. For a team that wants `view-source` transparency and zero build failures, the hidden React layer is friction.

### 6.3 NiceGUI

Source: [Slashdot NiceGUI vs Solara comparison](https://slashdot.org/software/comparison/NiceGUI-vs-Solara/)

> "NiceGUI is an open-source library designed for Python that empowers developers to craft web-based graphical user interfaces (GUIs) using solely Python code... constructed on FastAPI for backend functions, utilises Vue.js for frontend interactions, and incorporates Tailwind CSS for styling aesthetics."

NiceGUI is strong for simple dashboards and IoT/robotics tools. The Vue.js layer introduces a JS framework dependency and makes fine-grained Jinja template control harder to achieve. Not a natural fit for a team that wants Jinja partials as the unit of composition.

### 6.4 Streamlit

Streamlit is single-column, Python-widget-focused, and generates declarative re-renders on every interaction. It is not well-suited to multi-pane agent dashboards with precise visual hierarchy requirements. The visual-polish-system scoring dimensions (Spatial Breathing, Consistent Density, Component Cohesion) would be hard to enforce in Streamlit's layout model.

### 6.5 FastUI / Solara

FastUI renders Pydantic models into React components — similar to Reflex in that the final render is React. Solara merges ReactJS concepts with Python. Both inherit React build complexity. Neither is the right fit for the existing Python-deterministic architecture.

**Stack Verdict:** FastAPI + HTMX + Jinja2 + Tailwind CSS is the stack most compatible with: (a) the existing Python-first codebase, (b) a token system enforced in CSS variables, (c) Jinja partials as AI-composable components, (d) zero JS build step, (e) the scoring engine running server-side after render.

---

## 7. Component Library Patterns for Deterministic UI

### 7.1 The shadcn/ui Philosophy (Applicable Lessons for Python)

Source: [shadcn/ui documentation](https://ui.shadcn.com/docs)

> "**This is not a component library. It is how you build your component library.**"

> "shadcn/ui hands you the actual component code. You have full control to customize and extend the components to your needs. Full Transparency: You see exactly how each component is built. Easy Customization: Modify any part of a component to fit your design and functionality requirements. AI Integration: Access to the code makes it straightforward for LLMs to read, understand, and even improve your components."

> "Every component in shadcn/ui shares a common, composable interface. If a component does not exist, we bring it in, make it composable, and adjust its style to match and work with the rest of the design system. A shared, composable interface means it's predictable for both your team and LLMs. You are not learning different APIs for every new component."

> "The design of shadcn/ui makes it easy for AI tools to work with your code. Its open code and consistent API allow AI models to read, understand, and even generate new components. An AI model can learn how your components work and suggest improvements or even create new components that integrate with your existing design."

The lessons that transfer to Python/Jinja without the JS dependency:
1. Own the source of each component — no black-box library
2. Consistent interface contract across all components
3. AI works best when it can see the actual template code, not an API
4. Schema-driven distribution (in Python: a `components/` directory with documented Jinja macros)

### 7.2 AI-Friendly Component Design Principles

Source: [Creative Tim — shadcn/ui block libraries for AI](https://www.creative-tim.com/blog/open-source/5-best-open-source-shadcn-ui-block-libraries-ready-for-ai/)

> "What makes these libraries especially valuable today is that they all provide **registries**, **support MCP**, and are **ready for AI-powered workflows**. These features let AI models selectively fetch components and assets, improving reliability and helping avoid 'run-out-of-tokens' problems during generation. Because components can be pulled on demand, AI-driven and agent-based systems can iterate intelligently making UI workflows more predictable and maintainable."

The Python equivalent: a `components/` registry with Jinja macros, a `COMPONENTS.md` manifest describing each macro's signature and allowed parameters, and a `tokens.css` that defines every design token. AI reads the manifest, not the rendered HTML.

### 7.3 Prompt Templates as PRDs

Source: [UXMagic](https://uxmagic.ai/blog/production-ready-ai-design-prompts-saas):

> "Start writing prompts like PRDs. Anchor generation with real structure. Refine locally, not destructively. Demand code-ready output."

For the Amplified Partners system, this means each AI-generated component request should specify: which Jinja macro to use (or extend), which Tailwind utility classes are locked, which tokens are required, and what the data shape is. The AI fills in the layout logic for that specific data shape — not the design system itself.

---

## 8. The 10% Magic — What to Deliberately Leave to AI

### 8.1 The Generic AI Output Problem

Source: [UXMagic AI design prompts](https://uxmagic.ai/blog/production-ready-ai-design-prompts-saas):

> "If you don't define structure, AI defaults to statistical averages: Dark sidebar. 4 symmetrical KPI cards. Random line chart. Airy spacing. Zero hierarchy."

This describes the 0% scenario — no constraints at all. The 10% magic is not "let AI design freely." It is the specific decisions that are genuinely context-dependent and where AI adds value over a lookup table:

### 8.2 What AI Should Decide

**Layout intuition for specific data shapes:** Given a data schema (e.g., 3 time-series metrics + 1 binary status + 1 categorical distribution), AI selects whether to use a 3-column grid, a 2+1 split, or a vertical list — because the optimal choice depends on the number of dimensions, the relative importance of each metric, and the density expectation for the current view. This is genuine layout judgment, not rule lookup.

**Micro-copy:** Label text for empty states, loading messages, error descriptions, contextual headings. These depend on the specific agent task at hand. A rule cannot anticipate all states of Hermes or Mirror.

**Contextual emphasis:** Which metric in a given view gets primary visual weight (large type, high contrast) versus secondary. The scoring engine validates that the emphasis is correctly implemented, but AI decides which element in a novel view deserves top billing.

**Progressive disclosure decisions:** For a given data density, AI decides which details to show at first glance versus on hover/expand — because this depends on the cognitive context of the agent operating the dashboard, not a universal rule.

Source: [ELVTR designer's guide to AI tools 2025](https://uk.elvtr.com/blog/a-designers-guide-to-2025s-ai-tools):

> "Curation & Taste (Editing): AI excels at generating options, often hundreds of them. The designer's crucial role is to act as an editor, using their trained aesthetic judgment and 'taste' to identify the 1% of outputs that have real potential."

In the 90/10 system, the curation role is played by the scoring engine (UIClip + rubric normalised, composite = UIClip × 0.4 + rubric_normalised × 0.6). AI generates; the engine validates.

---

## OPINION SECTION
### Recommendation: Stack, LLM, Component Shape, Lock/Leave, Anti-Bloat

*All claims marked with confidence percentage. This section is opinion — not primary source research.*

---

#### Recommended Python Stack

**FastAPI + HTMX + Jinja2 + Tailwind CSS + Alpine.js.** [95% confidence]

This is the stack most coherent with the existing 187k Python LOC, the server-rendered scoring pipeline, and the Spine 5 90/10 architecture. It requires zero JS build step, produces auditable HTML (the scoring engine can parse rendered output or be invoked server-side before render), and keeps the full stack in a language the team already owns.

Tailwind CSS is the right utility layer because: (a) its class names map directly to design tokens (spacing, colour, typography) that can be locked via a Tailwind config file, making AI deviation from the token system syntactically impossible — the AI can only use classes that exist in the config, (b) it requires no CSS authoring skill from AI, just class composition, and (c) the existing visual-polish-system spacing grid (4px/8px multiples to 96px) maps cleanly to Tailwind's default spacing scale.

**Do not use Reflex, NiceGUI, or Solara** for this use case. They all introduce JS framework layers that: (a) are invisible to a Python-side scoring engine, (b) require JS build steps, and (c) make Jinja partials impossible as the compositional unit. [90% confidence]

---

#### Recommended LLM for UI Generation

**Claude Sonnet (current generation) for component generation; optionally Gemini 2.5 Pro for upstream planning.** [80% confidence]

The primary evidence is instruction-following fidelity under a strict spec. Claude altered only specified files with a flawless task completion rate vs Gemini's 78% unsolicited-file-modification rate (per the controlled $104 test cited in section 5). For a system where the 90% is locked and AI is only filling the 10% interstices, a model that respects boundaries is more valuable than a model that generates more content.

Claude Sonnet is the default recommendation over Opus for cost efficiency on high-volume component generation. Use Opus only for novel component types that require deep reasoning about data-shape-to-layout mapping. [75% confidence]

---

#### Shape of the Component System

**A Jinja macro library with a COMPONENTS.md manifest.** [90% confidence]

A "component" in this Python world is a **Jinja2 macro** in a `components/` directory — a parameterised template function with a documented signature. Example:

```jinja
{# components/metric_card.html #}
{% macro metric_card(label, value, trend=None, size="md", emphasis=False) %}
  <div class="rounded-lg bg-surface p-4 {{ 'shadow-elevation-2' if emphasis else 'shadow-elevation-1' }}">
    <p class="text-label-sm text-secondary">{{ label }}</p>
    <p class="text-{{ 'display-sm' if emphasis else 'headline-md' }} text-primary">{{ value }}</p>
    {% if trend is not none %}
      <span class="text-label-xs {{ 'text-positive' if trend > 0 else 'text-negative' }}">{{ trend }}%</span>
    {% endif %}
  </div>
{% endmacro %}
```

The `COMPONENTS.md` manifest lists every macro, its parameters, allowed values, which visual-polish-system dimensions it touches, and example invocations. An AI generating a new view reads the manifest, selects macros, and writes only the assembly logic — not the component internals.

**How the rubric enforces conformance:** The scoring engine is already built. The conformance mechanism at the generation layer is: (a) locked Tailwind config (the 90% — AI cannot use spacing, colour, or typography values not in the config), (b) linted Jinja templates (a CI check that macros are called with valid parameters), and (c) automated scoring on the rendered output before merge.

**How AI invokes it:** AI receives the `COMPONENTS.md` manifest as context, the data schema for the view it is generating, and a one-line brief. It outputs Jinja template code that assembles macros. It does not edit macro internals. The layout logic is the 10%. [85% confidence]

---

#### What to Lock in Deterministic Code (The 90%)

1. **Design tokens** — Tailwind config: spacing scale (4/8/12/16/24/32/48/64/80/96px), colour palette (LCH tokens mapped to sRGB CSS variables), type scale (Geist 11/12/14/16/20/24/32/40/48px), motion (50/100/200/300/500ms), shadow levels (0–4).
2. **Macro contracts** — every UI element exists as a macro with typed parameters. No raw HTML allowed outside macros in AI-generated templates.
3. **WCAG AA floor** — contrast ratios baked into the colour tokens (no token with <4.5:1 for text, <3:1 for UI components). Focus styles on all interactive macros. `prefers-reduced-motion` wrapper in the global CSS.
4. **Grid structure** — the 8-point base grid as Tailwind spacing, enforced by linting that AI cannot use arbitrary pixel values.
5. **Hard rules from the visual-polish-system** — the 9 existing hard rules continue to apply as CI gates. AI-generated templates must pass all 9.
6. **Component cohesion** — macros share consistent API shapes (every card-like macro takes `size`, `emphasis`, `label`; every status macro takes `state` with an enum).

[92% confidence across all six]

---

#### What to Leave for AI Magic (The 10%)

1. **Layout composition for novel data shapes** — given a new data schema, AI selects which macros to use and how to arrange them on the page grid. It does not invent new macros; it arranges existing ones.
2. **Empty state and loading micro-copy** — contextual to the specific agent task. AI writes the label text.
3. **Progressive disclosure decisions** — AI decides which data to show at first glance vs. on expand/hover, given the cognitive context of the view.
4. **Relative emphasis** — which metric in a novel view gets `emphasis=True` on its macro call. AI judgment, validated by the scoring engine.
5. **Contextual heading/label text** — titles, section headers, action labels for a specific dashboard view.

[88% confidence]

---

#### What Would Be Bloat

- **Any JS component library** (Radix, shadcn/ui as a runtime dependency, Headless UI) — the stack is server-rendered Jinja. These libraries are irrelevant and would require adding React or Vue. [99% confidence bloat]
- **Streamlit or Gradio** — wrong layout model for multi-pane agent dashboards with precise hierarchy requirements. [98% confidence bloat]
- **A separate design-token format** (e.g., Style Dictionary, Theo) — the visual-polish-system already defines the tokens. Map them directly to Tailwind config and CSS custom properties. Adding a token pipeline tool is an extra translation layer with no benefit. [90% confidence bloat]
- **An LLM that generates full components from scratch** — the 90/10 system means AI should never be generating macro internals. A model that is good at writing "full components from scratch" (e.g., Gemini in planning mode) is actually a risk in this context because it is more likely to deviate from the locked spec. [85% confidence bloat]
- **New scoring dimensions beyond the existing 10** — the visual-polish-system spec is 2006 lines. It is complete. Adding dimensions to an already-passing 66-test suite is scope creep. [99% confidence bloat]

---

*Signed: Cassian-research-subagent, 2026-05-05*
