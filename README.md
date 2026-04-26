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
└── examples/                  # Top level examples directory
    ├── bnh/py/                # Multi-objective — BNH problem (NSGA-II, Z3, PySMT)
    ├── c3dtlz4/py/            # Multi-objective optimzation benchmark problem — C3-DTLZ4 (Optuna GP Sampler)
    ├── cattlefeed/py/         # Global nonlinear constrained single objective optimization — HS73 cattle feed problem (SHGO)
    ├── constraint_dora/py/    # Constrained minimization schoolbook example (SLSQP)
    ├── deap/py/               # Constrained single-objective optimization using genetic algorithm (DEAP)
    ├── eggholder/py/          # Global unconstrained single-objective optimization — Eggholder function (SHGO, Dual Annealing)
    ├── pyomo/py/              # Solver comparison site for single- and multi-objective optimization 
    |                          # Algorithms used: large scale linear programming (GLPK)
    |                          #                  large scale non-linear optimization (IPOPT)
    |                          #                  genetic multiobjective optimization (NSGA-II and NSGA-III)
    |                          #                  mixed integer linear and non-linear programming (SCIP)
    └── shekel/py/             # Global black-box function optimization — Shekel function (SHGO)
                               # Two packages is used for building the model: Keras/TensorFlow and PyTorch

```

## 🧪 Examples

### 1. 🔴 BNH Problem — Multi-Objective Optimization
**Path:** `pyoptiwize/examples/bnh/py/`

Binh and Korn constrained bi-objective problem. Pareto front approximated with NSGA-II; Pareto-stable solutions certified using Z3 SMT solver and PySMT (gradient-stable and minimax-stable flavors).

- **Type:** Multi-objective, constrained (2 objectives, 2 constraints)
- **Solvers:** NSGA-II (pymoo), Z3, PySMT
- 📖 [pymoo BNH](https://pymoo.org/problems/multi/bnh.html)

---

### 2. 🟣 C3-DTLZ4 — Constrained Multi-Objective Benchmark
**Path:** `pyoptiwize/examples/c3dtlz4/py/`

Scalable constrained benchmark combining DTLZ4 objectives (α=100 density bias) with C3-type constraints. Solved with Optuna's Gaussian Process Sampler.

- **Type:** Multi-objective, constrained, scalable (m objectives, n variables)
- **Solver:** Optuna GP Sampler
- 📖 [Deb et al. DTLZ](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/145762/eth-24696-01.pdf)

---

### 3. 🟠 Cattle Feed Problem (HS73) — Nonlinear Programming
**Path:** `pyoptiwize/examples/cattlefeed/py/`

Hock–Schittkowski test problem #73. Minimizes a linear feed cost subject to nutritional linear, nonlinear, and equality constraints over 4 variables.

- **Type:** NLP, mixed linear/nonlinear constraints
- **Known minimum:** f(x\*) ≈ 29.894
- **Recommended solvers:** IPOPT, SQP, interior point methods
- 📖 [Reference](https://link.springer.com/book/10.1007/978-3-642-48320-2)

---

### 4. 🟢 Constraint Dora — Constrained Minimization
**Path:** `pyoptiwize/examples/constraint_dora/py/`

Textbook constrained minimization: minimize (x₁−2)² + (x₂−1)² subject to x₁² + x₂² ≤ 1. Solved with SLSQP; result verified analytically.

- **Type:** Single-objective, nonlinear constraint
- **Solver:** SLSQP
- 📖 [WolframAlpha solution](https://www.wolframalpha.com/input?i=Minimize%3A+f%28x1%2C+x2%29+%3D+%28x1+-+2%29%5E2+%2B+%28x2+-+1%29%5E2+subject+to+x1%5E2+%2B+x2%5E2+-+1+%3C%3D+0)

---

### 5. 🟤 DEAP — Constrained Single-Objective Optimization
**Path:** `pyoptiwize/examples/deap/py/`

Production planning problem with four products (A–D) and three shared resources (labor hours, machine hours, storage space). A genetic algorithm maximises total profit subject to resource capacity, minimum production quantities, a total weight limit, and a product ratio constraint. Infeasible individuals are steered towards feasibility via a graduated penalty in the fitness function rather than outright rejection.

- **Type:** Single-objective, constrained
- **Solver:** DEAP `eaSimple` (generational GA — blend crossover, Gaussian mutation, tournament selection)
- 📖 [Fortin et al., DEAP: Evolutionary Algorithms Made Easy, JMLR 2012 (PDF)](https://www.jmlr.org/papers/volume13/fortin12a/fortin12a.pdf)

---

### 6. 🟡 Eggholder Function — Global Optimization
**Path:** `pyoptiwize/examples/eggholder/py/`

Highly non-convex 2D benchmark with many local minima. Compares SHGO and Dual Annealing; includes 3D visualization and dataset generation.

- **Type:** Single-objective, unconstrained, global
- **Known minimum:** f(x\*) ≈ −959.64 at x\* ≈ (512, 404.23)
- **Solvers:** SHGO, Dual Annealing
- 📖 [Reference](https://www.sfu.ca/~ssurjano/egg.html)

---

### 7. 🔷 Pyomo - Solver Comparison Suite for Single Objective and Multiobjective Optimization
**Path:** `pyoptiwize/examples/pyomo/py/`

Comprehensive multi-solver comparison on the BNH problem and mixed-variable problems. Includes Pareto front approximation from CSV data using linear interpolation and decision trees, and direct solver comparisons.

- **Type:** Multi-objective & single-objective, constrained
- **Solvers:** NSGA-II, NSGA-III, SCIP, IPOPT, GLPK
- **Highlights:**
  - BNH Pareto front: analytical vs. linear interpolation vs. decision tree
  - Mixed-variable Pareto fronts (NSGA-II, NSGA-III)
  - Single-objective: SCIP vs. IPOPT comparison
  - Multi-objective: SCIP vs. NSGA-II comparison
  - Linear programming via GLPK

---

### 8. 🔵 Shekel Function — Global Optimization
**Path:** `pyoptiwize/examples/shekel/py/`

Classic 4-dimensional multimodal benchmark with 10 local minima. Solved with SciPy's SHGO algorithm using Sobol sampling.

- **Type:** Single-objective, unconstrained, global
- **Known minimum:** f(x\*) ≈ −10.5363 at x\* ≈ [4, 4, 4, 4]
- **Solver:** SHGO (Simplicial Homology Global Optimization)
- 📖 [Reference](https://www.sfu.ca/~ssurjano/shekel.html)

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

#### 3.1 python3.11

```bash
python3.11 -m venv_311 venv_311
source venv_311/bin/activate
```

#### 3.2 python3.12

```bash
python3 -m venv_312 venv_312
source venv_312/bin/activate
```

#### 3.3 python3.13

```bash
python3.13 -m venv_313 venv_313
source venv_313/bin/activate
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
python3 ./eggholder/py/optimization_ex.py
```

Expected results:

![Eggholder plot](https://raw.githubusercontent.com/mdmitry1/optimization-tutorial/master/media/Eggholder_plot.png)

```bash
The first element of the sorted dataset:     512.0 404.00 -959.5797
Analytical solution [1]:                     512.0 404.23 -959.6407
Simplicial homology global optimization [2]: 512.0 404.23 -959.6407
Dual annealing [3]:                          482.4 432.88 -956.9182
Difference between SHGO and DA methods: -2.84e-01 %
[1] EGGHOLDER: https://www.sfu.ca/~ssurjano/egg.html
[2] SHGO: https://link.springer.com/article/10.1007/s10898-018-0645-y
[3] DA: https://www.jstatsoft.org/article/view/v060i06
[4] SCIPY: https://docs.scipy.org/doc/scipy/tutorial/optimize.html#global-optimization
54e5105d59a57fd2898e581ca6f1e3502d4cda22b371fa17a88420d6da862602
```

### 6. Run all tests using existing virtual environment batch mode or interactively (requires installation with test dependencies)

`pip install` runs in virtual environment and therefore it is necessary to exit it before running tests

```bash
exit
$(python -c 'import pyoptiwize; print(pyoptiwize.__path__[0])')/../bin/run_optimization_tutorial_examples [-j]
```

- If -j option is specified, then Jupyter server will open

---

### 7. Full list of script options

```bash
run_optimization_tutorial_examples [[-h|--help] | [-clean] | [-w|--from_wheel] [-r|--force_reinstall] [-p|--python_version <version>]
                                   -h --help:             display this help message
                                   -clean:                clean all workareas /home/mdmitry/github/optimization_tutorial/bin/venv_31*
                                   -w --from_wheel:       install pyoptiwize from wheel https://pypi.org/project/pyoptiwize
                                   -r --force_reinstall:  reinstall pyoptiwize in existing workarea
                                   -p --python_version:   use python<version>
                                   -j --run_jupyter:      start jupyter notebook server
Supported python versions: python3.11 python3.12 python3.13
Default installation:      download git repository from the GitHub and then install from the latest version
Default python version:    python3.12
Workarea root directory:   /home/mdmitry/github/optimization_tutorial/bin/venv_31[1|2|3]
```

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

- Installation with test dependencies

```bash
pip install 'pyoptiwize[test]'
```
## ⚡ Recommended GUI support for Docker Image

### Native Linux

[Enter container using socat and X11 forwarding](https://github.com/mdmitry1/optimization-tutorial/blob/main/bin/enter_container_x11_forwarding)

### Windows 11 with WSL2 and WSG installed

[Enter container using WSLG X11 forwarding](https://github.com/mdmitry1/optimization-tutorial/blob/main/bin/enter_container_wslg)

---

## 🤖 AI-Powered Problem Formulator

`pyoptiwize` ships with an **optimization problem formulator** - an AI assistant that takes a plain-English description of your problem and returns a structured analysis, solver recommendation, and a ready-to-run Python script.

### Recommended System Prompt

```
You are an optimization problem formulator assistant for the `pyoptiwize` Python package.
When the user describes an optimization problem in plain English, respond with:

1. Problem analysis -  a small table with: problem type, objectives, constraints, variables
2. Solver recommendation - the best matching pyoptiwize example and solver, with 2-3 sentences explaining why
3. Generated Python script - a complete runnable script with all imports, realistic placeholder values, under 60 lines

pyoptiwize examples available:

* `bnh/py` - multi-objective constrained, NSGA-II / Z3 / PySMT
* `c3dtlz4/py` - scalable multi-objective benchmark, Optuna GP Sampler
* `cattlefeed/py` - NLP mixed constraints single-objective, SHGO / IPOPT
* `constraint_dora/py` - single-objective nonlinear constraint, SLSQP
* `deap/py` - constrained single-objective GA, DEAP eaSimple
* `eggholder/py` - global unconstrained single-objective, SHGO / Dual Annealing
* `pyomo/py` - multi-solver comparison, NSGA-II / NSGA-III / SCIP / IPOPT / GLPK
* `shekel/py` - 4D multimodal global optimization, SHGO

Start by greeting the user and inviting them to describe their optimization problem.
```

### [Example Claude AI session](https://claude.ai/share/295a4dd0-0039-4b1c-8145-5cab4cd1b22e)

---

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

- [BNH problem — pymoo](https://pymoo.org/problems/multi/bnh.html)
- [C3-DTLZ4 source code](https://github.com/optuna/optunahub-registry/blob/main/package/benchmarks/dtlz_constrained/_dtlz_constrained.py)
- [DEAP API](https://deap.readthedocs.io/en/master/api/algo.html)
- [Shekel function](https://www.sfu.ca/~ssurjano/shekel.html)
- [Eggholder function](https://www.sfu.ca/~ssurjano/egg.html)
- [GLPK](https://en.wikipedia.org/wiki/GNU_Linear_Programming_Kit)
- [Hock & Schittkowski test problems](https://link.springer.com/book/10.1007/978-3-642-48320-2)
- [IPOPT](https://github.com/coin-or/Ipopt)
- [NSGA-II](https://sci2s.ugr.es/sites/default/files/files/Teaching/OtherPostGraduateCourses/Metaheuristicas/Deb_NSGAII.pdf)
- [NSGA-III](https://www.egr.msu.edu/~kdeb/papers/k2012009.pdf)
- [Optuna GP Sampler](https://medium.com/optuna/introducing-optunas-native-gpsampler-0aa9aa3b4840)
- [pymoo](https://pypi.org/project/pymoo)
- [Pyomo](https://pypi.org/project/pyomo)
- [PySMT](https://pypi.org/project/PySMT)
- [SCIP](https://www.scipopt.org)
- [SLSQP](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html)
- [Z3](https://en.wikipedia.org/wiki/Z3_Theorem_Prover)

---

## Copyright and license

© 2025-2026 Dmitry Messerman. Licensed under [GNU General Public License v3.0](LICENSE).

