# The Entropic Zoo Protocol

A structural framework for analyzing optimization ecosystems.

This repository presents a conceptual taxonomy of feedback systems operating under varying degrees of self-reference and variance coupling. No empirical validation is included here.

---

## Repository Structure
- **ABSTRACT.md** — High-level conceptual summary.
- **DEFINITIONS.md** — Formal structural terminology and (S, V, P) tuples.
- **RELATED_WORK.md** — Alignment with current AI research (Model Collapse, GANs).
- **FAILURE_MODES.md** — Identification of system rupture points.
- **ORIGIN_AND_METHOD.md** — Neutral development methodology.
- **core/** — Detailed species taxonomy.

---

## Scope and Intent
This framework provides a structural lens for examining optimization trajectories. It does not assert the inevitability of collapse nor propose specific governance prescriptions.

### Usage: Running the Simulation

The repository includes a Python-based numerical simulation of the Support Contraction inequality ($P > B + V$).

### Prerequisites
Ensure you have Python 3 installed along with the required libraries:
```bash
pip install numpy matplotlib
ExecutionTo visualize the dynamical regimes (Collapse vs. Stability), run the following command from the root directory:Bashpython models/collapse_simulation.py
This will generate a plot showing the trajectory of Support Breadth ($B$) under different optimization and entropy parameters.