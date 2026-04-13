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

## 📂 Repository Structure

```
pyoptiwize/                        # repo root (cloned from optimization_tutorial)
├── pyproject.toml
├── conftest.py
├── LICENSE
├── pyoptiwize/                    # package directory
│   ├── config/                    # Environment setup & dependency notes
│   └── examples/
│       ├── shekel/py/             # Global optimization — Shekel function (SHGO)
│       ├── eggholder/py/          # Global optimization — Eggholder function (SHGO, Dual Annealing)
│       ├── constraint_dora/py/    # Constrained minimization (SLSQP)
│       ├── cattlefeed/py/         # Nonlinear constrained NLP — HS73 cattle feed problem
│       ├── bnh/py/                # Multi-objective — BNH problem (NSGA-II, Z3, PySMT)
│       ├── c3dtlz4/py/            # Multi-objective benchmark — C3-DTLZ4 (Optuna GP Sampler)
│       └── pyomo/py/              # Solver comparison — NSGA-II, SCIP, IPOPT, GLPK
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

## ⚡ Installation (Ubuntu 24.04)

### 1. System packages

```bash
sudo apt-get update && sudo apt-get install -y \
    g++ gcc git glpk-utils jq \
    libgfortran5 libgmp-dev libgomp1 libmpfr6 \
    locales tzdata \
    python3 python-is-python3 python3-dev python3-pip \
    python3-pytest-mock python3-setuptools python3-tk python3-venv \
    python3-z3 z3 \
    tcsh vim wget \
    x11-apps x11-xserver-utils xvfb
```

### 2. Python 3.11 and 3.13 (via deadsnakes PPA)

Ubuntu 24.04 ships Python 3.12 by default. Install 3.11 and 3.13 from the deadsnakes PPA:

```bash
sudo apt-get install -y gnupg curl ca-certificates

curl -fsSL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xF23C5A6CF475977595C89F51BA6932366A755776" \
    | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/deadsnakes.gpg > /dev/null

echo "deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble main" \
    | sudo tee /etc/apt/sources.list.d/deadsnakes.list

sudo apt-get update && sudo apt-get install -y \
    python3.11 python3.11-venv python3.11-dev python3.11-tk \
    python3.13 python3.13-venv python3.13-dev python3.13-tk
```

### 3. Miniconda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh -b
```

Accept the Conda terms of service:

```bash
~/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
~/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
```

### 4. SCIP and IPOPT

```bash
~/miniconda3/bin/conda install -y -c conda-forge ipopt scip
sudo ln -sf ~/miniconda3/bin/scip /usr/local/bin/scip
sudo ln -sf ~/miniconda3/bin/ipopt /usr/local/bin/ipopt
```

### 5. MathSAT (for PySMT / Z3 stable-gradient examples)

> ⚠️ **Licensing limitations**
> Please read the [MathSAT 5 license terms](https://mathsat.fbk.eu/download.html) before using MathSAT.
> **MathSAT 5 is available for research and evaluation purposes only. It cannot be used in a commercial environment, particularly as part of a commercial product, without written permission.** MathSAT 5 is provided as-is, without any warranty.

Download [MathSAT 5.6.15](https://mathsat.fbk.eu/download.html) and build the Python bindings for each interpreter:

```bash
wget https://mathsat.fbk.eu/release/mathsat-5.6.15-linux-x86_64.tar.gz

# Python 3.12 (system default)
tar -xf mathsat-5.6.15-linux-x86_64.tar.gz
cd mathsat-5.6.15-linux-x86_64/python
python setup.py build
sudo mkdir -p /usr/local/lib/python3.12/dist-packages
sudo mv mathsat.py /usr/local/lib/python3.12/dist-packages/
sudo mv build/lib.linux-x86_64-cpython-312/_mathsat.cpython-312-x86_64-linux-gnu.so \
        /usr/local/lib/python3.12/dist-packages/_mathsat.so
cd ../..

# Python 3.13
tar -xf mathsat-5.6.15-linux-x86_64.tar.gz
cd mathsat-5.6.15-linux-x86_64/python
python3.13 setup.py build
sudo mkdir -p /usr/local/lib/python3.13/dist-packages
sudo mv mathsat.py /usr/local/lib/python3.13/dist-packages/
sudo mv build/lib.linux-x86_64-cpython-313/_mathsat.cpython-313-x86_64-linux-gnu.so \
        /usr/local/lib/python3.13/dist-packages/_mathsat.so
cd ../..

# Python 3.11
tar -xf mathsat-5.6.15-linux-x86_64.tar.gz
cd mathsat-5.6.15-linux-x86_64/python
python3.11 setup.py build
sudo mkdir -p /usr/local/lib/python3.11/dist-packages
sudo mv mathsat.py /usr/local/lib/python3.11/dist-packages/
sudo mv build/lib.linux-x86_64-cpython-311/_mathsat.cpython-311-x86_64-linux-gnu.so \
        /usr/local/lib/python3.11/dist-packages/_mathsat.so
cd ../..

rm -rf mathsat-5.6.15-linux-x86_64 mathsat-5.6.15-linux-x86_64.tar.gz
```

### 6. Locale

```bash
sudo locale-gen en_US.UTF-8
```

Add to your `~/.bashrc` (or `~/.profile`):

```bash
export LANG=en_US.UTF-8
export LANGUAGE=en_US:en
export LC_ALL=en_US.UTF-8
```

### 7. Clone the repository

```bash
git clone https://github.com/mdmitry1/optimization_tutorial.git pyoptiwize
cd pyoptiwize
```

### 8. Install Python dependencies

Install the package and its dependencies from `pyproject.toml`:

```bash
# Standard install
pip install .

# With test dependencies
pip install ".[test]"
```

This installs the following key dependencies:

| Package | Version |
|---|---|
| PySMT | ~0.9.6 |
| DEAP | ~1.4.3 |
| pymoo | ~0.6.1 |
| Pyomo | ~6.9.5 |
| OptunaHub | ~0.4.0 |
| scikit-learn | ~1.8.0 |
| scikit-optimize | ~0.10.2 |
| pandas | ~2.3.3 |
| TensorFlow | ~2.20.0 |
| PyTorch | ~2.10.0 |
| ONNX Runtime | ~1.23.2 |
| shgo | ~1.0.0 |

Test extras (`.[test]`): `pytest ~9.0.3`, `pytest-forked ~1.6.0`, `pytest-mock ~3.15.1`

### 9. Run an example

```bash
cd pyoptiwize/examples/eggholder/py
python optimization_ex.py
```

### 10. Run tests

Some tests (Z3 and Keras-based) must run in forked subprocesses to isolate solver state. The `conftest.py` at the repo root automatically marks any test whose path contains `z3` or `keras` with the `forked` marker.

Run in two passes from each example's `py/` directory:

```bash
# Pass 1 — forked tests (z3, keras)
pytest -v --forked -m forked

# Pass 2 — all other tests
pytest -v -s -m 'not forked'
```

---

## 🛠️ Environment

| Component | Version |
|---|---|
| OS | Ubuntu 24.04 LTS (Noble) |
| Python | 3.11, 3.12, 3.13 |
| NumPy | 1.26.4 (py3.12) / 2.4.1 (py3.14) |
| SciPy | 1.16.3 |
| pymoo | 0.6.1.6 |
| Pyomo | 6.9.5 |
| Optuna | 4.7.0 |
| IPOPT | 3.14.19 |
| SCIP | 10.0.0 |
| GLPK | 5.0 |
| Z3 | 4.8.12 |
| CUDA | 12.8 |

Full environment details: [`pyoptiwize/config/README.md`](pyoptiwize/config/README.md)

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

## 📄 License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
