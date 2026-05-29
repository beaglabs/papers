# Canonical Entity IDs Paper

This directory contains the current paper draft for:

**Canonical Entity IDs for Grounded Action Generation**  
**A Reference Layer for Small Specialist Models over Structured State**

PDF for GitHub viewing:

- [Canonical_Entity_IDs_for_Grounded_Action_Generation.pdf](Canonical_Entity_IDs_for_Grounded_Action_Generation.pdf)

The draft is no longer a generic SSTT/pluggable-specialists paper. It is now a narrower paper about one claim:

> structured action generation often fails because models do not have a stable, consistent, model-friendly reference layer for entities.

The paper argues that **Canonical Entity IDs (CEIDs)** provide that layer.

## Paper Thesis

The core thesis is:

- small specialists can already learn structured action schemas
- the harder problem is grounding indirect references to the correct entity
- CEIDs make entity references shorter, typed, scoped, and reversible
- consistent alias rewriting across state, hints, and generated actions materially improves exact structured action generation

The current empirical anchor is the robotics `hard_v2` candidate-pressure slice.

## Current Quantitative Story

On the current 250-example robotics evaluation slice, the paper’s main ablation is:

| Variant | Valid JSON | Valid Schema | Exact Op | Exact Match |
| --- | ---: | ---: | ---: | ---: |
| Baseline specialist | 1.000 | 0.992 | 1.000 | 0.616 |
| Baseline + CEIDs and ranked hints | 1.000 | 0.856 | 1.000 | 0.660 |
| Prior row + consistent hint rewriting | 1.000 | 0.980 | 1.000 | 0.968 |
| Prior row + parser and action normalization | 1.000 | 0.992 | 1.000 | 0.980 |

That progression is the heart of the draft:

- baseline fails mainly on entity grounding
- CEIDs help immediately
- inconsistent rewriting can break the benefits
- once the alias space is fully consistent, performance jumps sharply

## What This Paper Is and Is Not

### This paper is

- a paper about identity/reference design for structured action generation
- a paper about grounded specialist behavior over structured state
- a paper with robotics as the main empirical domain

### This paper is not

- a full general theory of pluggable experts
- a broad Murmuration theory paper
- a general agent paper
- a paper claiming real-world robotics deployment

The broader specialist-routing and Murmuration ideas still matter, but in this draft they are background framing, not the primary contribution.

## File Map

- [Canonical_Entity_IDs_for_Grounded_Action_Generation.pdf](Canonical_Entity_IDs_for_Grounded_Action_Generation.pdf) — compiled PDF for GitHub's PDF viewer
- [main.tex](main.tex) — paper source
- [references.bib](references.bib) — bibliography
- [figures/ceid_flow.tex](figures/ceid_flow.tex) — dedicated CEID pipeline figure
- [figures/robotics_coordination.tex](figures/robotics_coordination.tex) — robotics world/action figure
- [figures/architecture_flow.tex](figures/architecture_flow.tex) — older broader systems figure; optional now
- [figures/rust_grounding.tex](figures/rust_grounding.tex) — archived Rust figure; no longer primary
- [minted-demo/](minted-demo/) — optional code-snippet staging area

## Build

This paper uses:

- `minted` for code listings
- `tikz` / `pgfplots` for figures
- `natbib` for references

Because `minted` shells out to Pygments, build with `-shell-escape`.

### Recommended build

```bash
cd papers/sstt-paper
latexmk -pdf -shell-escape main.tex
```

### Local prerequisite

```bash
python3 -m pip install Pygments
```

## Draft Structure

The current draft is organized to keep the claim narrow:

1. `Introduction`
   Defines the grounding problem and positions CEIDs as the missing reference layer.

2. `Problem Setting`
   Explains why indirect references break structured action generation.

3. `Canonical Entity IDs`
   Defines the alias format, design goals, and consistency requirement.

4. `System Overview`
   Shows where CEIDs sit in the runtime-to-model-to-validator path.

5. `Experimental Setup`
   Describes the robotics domain and harder candidate-pressure slice.

6. `Results`
   Presents the cumulative CEID ablation and error story.

7. `Discussion`
   Interprets CEIDs as a concrete primitive inside broader specialist systems.

8. `Limitations` and `Next Experiments`
   Keeps the claims honest and scoped.

## Writing Guidance

When editing this draft, preserve these priorities:

- keep CEIDs as the headline contribution
- keep routing and Murmuration subordinate
- keep the quantitative story centered on the hard robotics slice
- explicitly describe the hint-rewrite bug and why it mattered
- avoid drifting back into a broad “pluggable experts” paper

## Immediate Next Improvements

The highest-value paper improvements now are:

- compile the PDF and clean up layout issues
- add or refine one CEID-specific figure if needed after the build
- tighten the language around the ablation table if reviewers/readers could misread the cumulative progression
- Rust specialist has been removed from the repo; keep CEID paper focused on robotics
- replace the 250-example slice with a fuller held-out evaluation once that result is stable and reproducible
