# Python Optimization Cookbook

![Python](https://img.shields.io/badge/Python-3.11%20|%203.12%20|%203.13-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.26%2B-013243?logo=numpy)
![SciPy](https://img.shields.io/badge/SciPy-1.16%2B-8CAAE6?logo=scipy)
![pymoo](https://img.shields.io/badge/pymoo-0.6.1-orange)
![Pyomo](https://img.shields.io/badge/Pyomo-6.9-blue)
![Optuna](https://img.shields.io/badge/Optuna-4.7-6C5CE7)
![pytest](https://img.shields.io/badge/tested%20with-pytest-yellow?logo=pytest)

A collection of hands-on optimization examples covering single-objective, multi-objective, constrained, and benchmark problems — implemented in Python with solvers including SciPy, pymoo, Pyomo, SCIP, IPOPT, GLPK, Optuna, and Z3.

---

## 📂 Package structure

```
pyoptiwize/                    # Package root directory
├── config/                    # Python dependency trees
└── examples/
    ├── shekel/py/             # Global optimization — Shekel function (SHGO)
    ├── eggholder/py/          # Global optimization — Eggholder function (SHGO, Dual Annealing)
    ├── constraint_dora/py/    # Constrained minimization (SLSQP)
    ├── cattlefeed/py/         # Nonlinear constrained NLP — HS73 cattle feed problem
    ├── bnh/py/                # Multi-objective — BNH problem (NSGA-II, Z3, PySMT)
    ├── c3dtlz4/py/            # Multi-objective benchmark — C3-DTLZ4 (Optuna GP Sampler)
    └── pyomo/py/              # Solver comparison — NSGA-II, SCIP, IPOPT, GLPK
```

---

## 🧪 Examples

### 1. 🔵 Shekel Function — Global Optimization
**Path:** `pyoptiwize/examples/shekel/py/`

Classic 4-dimensional multimodal benchmark with 10 local minima. Solved with SciPy's SHGO algorithm using Sobol sampling.

- **Type:** Single-objective, unconstrained, global
- **Known minimum:** f(x\*) ≈ −10.5363 at x\* ≈ [4, 4, 4, 4]
- **Solver:** SHGO (Simplicial Homology Global Optimization)
- 📖 [Reference](https://www.sfu.ca/~ssurjano/shekel.html)

---

### 2. 🟡 Eggholder Function — Global Optimization
**Path:** `pyoptiwize/examples/eggholder/py/`

Highly non-convex 2D benchmark with many local minima. Compares SHGO and Dual Annealing; includes 3D visualization and dataset generation.

- **Type:** Single-objective, unconstrained, global
- **Known minimum:** f(x\*) ≈ −959.64 at x\* ≈ (512, 404.23)
- **Solvers:** SHGO, Dual Annealing
- 📖 [Reference](https://www.sfu.ca/~ssurjano/egg.html)

---

### 3. 🟢 Constraint Dora — Constrained Minimization
**Path:** `pyoptiwize/examples/constraint_dora/py/`

Textbook constrained minimization: minimize (x₁−2)² + (x₂−1)² subject to x₁² + x₂² ≤ 1. Solved with SLSQP; result verified analytically.

- **Type:** Single-objective, nonlinear constraint
- **Solver:** SLSQP
- 📖 [WolframAlpha solution](https://www.wolframalpha.com/input?i=Minimize%3A+f%28x1%2C+x2%29+%3D+%28x1+-+2%29%5E2+%2B+%28x2+-+1%29%5E2+subject+to+x1%5E2+%2B+x2%5E2+-+1+%3C%3D+0)

---

### 4. 🟠 Cattle Feed Problem (HS73) — Nonlinear Programming
**Path:** `pyoptiwize/examples/cattlefeed/py/`

Hock–Schittkowski test problem #73. Minimizes a linear feed cost subject to nutritional linear, nonlinear, and equality constraints over 4 variables.

- **Type:** NLP, mixed linear/nonlinear constraints
- **Known minimum:** f(x\*) ≈ 29.894
- **Recommended solvers:** IPOPT, SQP, interior point methods
- 📖 [Reference](https://link.springer.com/book/10.1007/978-3-642-48320-2)

---

### 5. 🔴 BNH Problem — Multi-Objective Optimization
**Path:** `pyoptiwize/examples/bnh/py/`

Binh and Korn constrained bi-objective problem. Pareto front approximated with NSGA-II; Pareto-stable solutions certified using Z3 SMT solver and PySMT (gradient-stable and minimax-stable flavors).

- **Type:** Multi-objective, constrained (2 objectives, 2 constraints)
- **Solvers:** NSGA-II (pymoo), Z3, PySMT
- 📖 [pymoo BNH](https://pymoo.org/problems/multi/bnh.html)

---

### 6. 🟣 C3-DTLZ4 — Constrained Multi-Objective Benchmark
**Path:** `pyoptiwize/examples/c3dtlz4/py/`

Scalable constrained benchmark combining DTLZ4 objectives (α=100 density bias) with C3-type constraints. Solved with Optuna's Gaussian Process Sampler.

- **Type:** Multi-objective, constrained, scalable (m objectives, n variables)
- **Solver:** Optuna GP Sampler
- 📖 [Deb et al. DTLZ](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/145762/eth-24696-01.pdf)

---

### 7. 🔷 Pymoo & Pyomo — Solver Comparison Suite
**Path:** `pyoptiwize/examples/pyomo/py/`

Comprehensive multi-solver comparison on the BNH problem and mixed-variable problems. Includes Pareto front approximation from CSV data using linear interpolation and decision trees, and direct solver comparisons.

- **Type:** Multi-objective & single-objective, constrained
- **Solvers:** NSGA-II, NSGA-III, SCIP, IPOPT, GLPK
- **Highlights:**
  - BNH Pareto front: analytical vs. linear interpolation vs. decision tree
  - Mixed-variable Pareto fronts (NSGA-II, NSGA-III)
  - Single-objective: SCIP vs. IPOPT comparison
  - Multi-objective: SCIP vs. IPOPT vs. NSGA-II comparison
  - Linear programming via GLPK/Pyomo

---

## ⚠️ **Licensing limitations - read before installation**

Please read the [MathSAT 5 license terms](https://mathsat.fbk.eu/download.html) before using MathSAT.
**MathSAT 5 is available for research and evaluation purposes only.**<br> 
**It cannot be used in a commercial environment, particularly as part of a commercial product, without written permission.**<br>
MathSAT 5 is provided as-is, without any warranty.

## ⚡ Installation (Ubuntu 24.04)

### 1. External dependencies

#### 1.1 Download installation script [install.bash](https://raw.githubusercontent.com/mdmitry1/optimization-tutorial/refs/heads/main/docker/24.04/install.bash)

#### 1.2. Run installation script (⚠️`sudo` required)
```bash
chmod +x install.bash
sudo ./install.bash
```

### 2. Set locale

```bash
export LANG=en_US.UTF-8
export LANGUAGE=en_US:en
export LC_ALL=en_US.UTF-8
```

### 3. Create and enter virtual environment
```bash
python3 -m venv_312 venv_312
source venv_312/bin/activate
```

### 4. Install `pyoptiwize`

- Standard installation
```bash
pip install pyoptiwize
```

- Installation with test dependencies
```bash
pip install 'pyoptiwize[test]'
```

### 5. Quickstart - run an example

```bash
cp -rp $(python -c 'import pyoptiwize; print(pyoptiwize.__path__[0])')/examples/eggholder .
./eggholder/py/optimization_ex.py
```

### 6. Run all tests using existing virtual environment (requires installation with test dependencies)

Installation script starts its own virtual environment and therefore it is necessary to exit current virtual environment before running tests

```bash
exit
$(python -c 'import pyoptiwize; print(pyoptiwize.__path__[0])')/../bin/run_optimization_tutorial_examples
```
---

## ⚡ Installation from Docker image

```bash
docker pull ghcr.io/mdmitry1/optimization-tutorial:latest
docker run -it ghcr.io/mdmitry1/optimization-tutorial:latest
python -m venv venv_312
bash
source venv_312/bin/activate
```

- Standard installation
```bash
pip install pyoptiwize
```

- Installion with test dependencies

```bash
pip install 'pyoptiwize[test]'
```

## 🛠️ Environment

| Component | Version |
|---|---|
| OS | Ubuntu 24.04 LTS (Noble) |
| Python | 3.11, 3.12, 3.13 |
| IPOPT | 3.14.19 |
| SCIP | 10.0.0 |
| GLPK | 5.0 |
| Z3 | 4.8.12 |
| CUDA | 12.8 |

---

## 📚 References

- [Shekel function](https://www.sfu.ca/~ssurjano/shekel.html)
- [Eggholder function](https://www.sfu.ca/~ssurjano/egg.html)
- [Hock & Schittkowski test problems](https://link.springer.com/book/10.1007/978-3-642-48320-2)
- [BNH problem — pymoo](https://pymoo.org/problems/multi/bnh.html)
- [NSGA-II](https://sci2s.ugr.es/sites/default/files/files/Teaching/OtherPostGraduateCourses/Metaheuristicas/Deb_NSGAII.pdf)
- [NSGA-III](https://www.egr.msu.edu/~kdeb/papers/k2012009.pdf)
- [C3-DTLZ4 source code](https://github.com/optuna/optunahub-registry/blob/main/package/benchmarks/dtlz_constrained/_dtlz_constrained.py)
- [SCIP solver](https://www.scipopt.org)
- [IPOPT](https://github.com/coin-or/Ipopt)
- [GLPK](https://en.wikipedia.org/wiki/GNU_Linear_Programming_Kit)
- [pymoo](https://pypi.org/project/pymoo)
- [Pyomo](https://pypi.org/project/pyomo)
- [Optuna GP Sampler](https://medium.com/optuna/introducing-optunas-native-gpsampler-0aa9aa3b4840)

---

## Copyright and license

© 2025-2026 Dmitry Messerman. Licensed under [GNU General Public License v3.0](LICENSE).

