# Graphical Abstract — specification

**File:** `paper/graphical-abstract.svg` — editable vector draft (no external fonts; system sans-serif).

**Layout (hybrid A+C redesign, no title):**
1. *Formula anchor* (top): $\eta_L = I_{\text{pred}}/N_{\text{max}}$ + one-line gloss + $N_{\text{max}}$ definition.
2. *Hero* (middle): paired loop diagrams — **closed self-payment loop** (η_L > 0, green: model M, own exergy, environment E, error returns as the system's own free-energy loss, all inside one boundary) vs **open externally-paid loop** (η_L = 0, grey: dissipation paid from an external grid/setpoint, the loop is visibly broken). This pair carries the central conceptual novelty visually.
3. *Strip* (bottom): a one-axis η_L line — a hard wall at η_L = 0 with the grey non-vital cluster (Sun, hurricane, crystal, LLM-at-inference, each a minimal vector icon), positive green points (city ≲3·10⁻³⁰, biosphere ≲10⁻¹⁸, bacterium ~3·10⁻⁸/3·10⁻⁵) with icons, and a dashed Bennett-demon ceiling at η_L → 1.
4. *Tagline band*: "Observable matter is structurally complex almost everywhere — and vital almost nowhere."

All icons are pure SVG primitives (no emoji/fonts/raster); all numbers match the paper
(§ 3.4–3.7) exactly. Fonts sized for thumbnail legibility; no in-figure title (MDPI convention).

**MDPI Entropy export requirements (production step):**
- Final raster: TIFF or PNG, RGB, **≥ 1000 px** on the shorter side, 300 dpi; or submit the vector.
- Aspect close to landscape; legible at thumbnail size; no copyrighted/third-party imagery (none used).
- Single panel, minimal text, no figure caption inside the file (MDPI convention).

**Status:** draft for review; conversion SVG → TIFF/PNG and any palette/typography polish is a
production-time task. Content is final and paper-consistent.
