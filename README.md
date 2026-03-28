# Binomial Calculator & Probability Toolkit

A comprehensive Python tool for calculating probabilities, permutations, combinations, and binomial distributions. This interactive toolkit provides powerful statistical calculations with clear, formatted output and educational explanations.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Core Concepts](#core-concepts)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Requirements](#requirements)
- [License](#license)

## ✨ Features

### 1. **Permutation & Combination Calculator**

- Calculate permutations P(n, r)
- Calculate combinations C(n, r)
- Display results as simplified fractions

### 2. **Binomial Distribution Solver**

- Calculate probability mass function (PMF): P(X = k)
- Compute cumulative probabilities: P(X ≤ k), P(X ≥ k), P(k₁ ≤ X ≤ k₂)
- Generate complete probability distribution tables
- Calculate binomial statistics (mean, variance, standard deviation)

### 3. **Educational Features**

- Clear mathematical formulas displayed with calculations
- Detailed step-by-step breakdowns
- Properties of binomial experiments explained

### 4. **User-Friendly Interface**

- Interactive menu-driven system
- Input validation with helpful error messages
- Professional formatted output with ASCII art separators
- Clear labeling of all results

## 💻 Installation

### Prerequisites

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

### Setup

1. Clone or download the repository:

```bash
git clone https://github.com/yourusername/Binomial_Calculator.git
cd Binomial_Calculator
```

2. Verify Python installation:

```bash
python --version
```

3. Run the program:

```bash
python bino.py
```

## 🚀 Usage

### Running the Program

```bash
python bino.py
```

The program provides a main menu with two options:

```
═════════════════════════════════════════════════════
  PROBABILITY TOOLKIT  —  Permutation, Combination & Binomial
═════════════════════════════════════════════════════

  MAIN MENU
  ────────────────────────────────────────────────────────
   1. Permutation & Combination (P and C)
   2. Binomial Experiment Solver
```

### Menu Options

#### Option 1: Permutation & Combination Calculator

- Enter values for n and r
- Get P(n,r) and C(n,r) with optimized fraction representations

#### Option 2: Binomial Experiment Solver

- Set number of trials (n) and probability (p)
- Choose from 5 query types:
  1. Exactly r successes: P(X = r)
  2. At most r successes: P(X ≤ r)
  3. At least r successes: P(X ≥ r)
  4. Between r₁ and r₂: P(r₁ ≤ X ≤ r₂)
  5. Full distribution table

## 📚 Core Concepts

### Binomial Distribution

A binomial distribution models the number of successes in a fixed number of independent trials, where each trial has exactly two outcomes (success or failure) with constant probability.

**Key Properties of a Binomial Experiment:**

1. Fixed number of trials (n), each identical and independent
2. Each trial has exactly two outcomes: success or failure
3. Probability of success (p) is constant across all trials
4. Trials are mutually independent of each other
5. Random variable X counts total successes in n trials
6. X ~ B(n, p) → PMF: P(X=k) = C(n,k) · p^k · q^(n-k)

### Key Formulas

**Probability Mass Function (PMF):**

```
P(X = r) = C(n, r) · p^r · (1-p)^(n-r)
```

**Mean (Expected Value):**

```
μ = n · p
```

**Variance:**

```
σ² = n · p · q  (where q = 1-p)
```

**Standard Deviation:**

```
σ = √(n · p · q)
```

**Permutation:**

```
P(n, r) = n! / (n-r)! = n × (n-1) × ... × (n-r+1)
```

**Combination:**

```
C(n, r) = n! / (r! × (n-r)!)
```

## 🔧 API Reference

### Helper Functions

#### `combination(n, r)`

- **Description:** Calculate number of combinations C(n, r)
- **Parameters:** n (int), r (int)
- **Returns:** int
- **Example:** `combination(5, 2)` → 10

#### `permutation(n, r)`

- **Description:** Calculate number of permutations P(n, r)
- **Parameters:** n (int), r (int)
- **Returns:** int
- **Example:** `permutation(5, 2)` → 20

#### `combination_fraction(n, r)`

- **Description:** Calculate combination and return as simplified fraction
- **Parameters:** n (int), r (int)
- **Returns:** tuple (numerator, denominator)

### Binomial Statistics

#### `pmf(n, p, r)`

- **Description:** Calculate probability mass function P(X = r)
- **Parameters:** n (int trials), p (float, success probability), r (int, successes)
- **Returns:** float (probability)

#### `binomial_mean(n, p)`

- **Description:** Calculate mean of binomial distribution
- **Parameters:** n, p
- **Returns:** float

#### `binomial_variance(n, p)`

- **Description:** Calculate variance of binomial distribution
- **Parameters:** n, p
- **Returns:** float

#### `binomial_std(n, p)`

- **Description:** Calculate standard deviation of binomial distribution
- **Parameters:** n, p
- **Returns:** float

### Probability Queries

#### `prob_exact(n, p, r)`

- **Description:** Calculate P(X = r)
- **Returns:** float

#### `prob_at_most(n, p, r)`

- **Description:** Calculate P(X ≤ r)
- **Returns:** float

#### `prob_at_least(n, p, r)`

- **Description:** Calculate P(X ≥ r)
- **Returns:** float

#### `prob_between(n, p, r1, r2)`

- **Description:** Calculate P(r₁ ≤ X ≤ r₂)
- **Returns:** float

### Display Functions

#### `print_distribution(n, p)`

- **Description:** Display complete probability distribution table

#### `print_stats(n, p, label="")`

- **Description:** Display mean, variance, and standard deviation

#### `print_features()`

- **Description:** Display the 6 key features of binomial experiments

## 📖 Examples

### Example 1: Simple Combination

```
Input:  n=5, r=2
Output: C(5,2) = 10
```

### Example 2: Coin Toss Probability

```
Setup: X ~ B(10, 0.5)  (10 coin tosses, p=0.5)

Query: What's the probability of exactly 7 heads?
P(X = 7) = C(10,7) · (0.5)^7 · (0.5)^3
         = 120 · 0.0078125 · 0.125
         = 0.117188  ≈  11.72%

Mean (μ)           = 10 · 0.5 = 5.0000
Variance (σ²)      = 10 · 0.5 · 0.5 = 2.5000
Std deviation (σ)  = √2.5 = 1.5811
```

### Example 3: Quality Control

```
Setup: Manufacturing with 5% defect rate, sample of 20 items
X ~ B(20, 0.05)

Query: Probability of finding at most 2 defects?
P(X ≤ 2) = P(X=0) + P(X=1) + P(X=2)
         = 0.358486 + 0.377305 + 0.188652
         = 0.924443  ≈  92.44%
```

## 📋 Requirements

- **Python:** 3.6+
- **Dependencies:** None (uses only standard library)
  - `math.gcd` - for fraction simplification
  - `math.sqrt` - for standard deviation
  - `math.factorial` - for combinations and permutations

## 🛠️ Customization

The code is modular and can be imported into other Python projects:

```python
from bino import prob_exact, binomial_mean, combination

# Use as a library
p = prob_exact(n=10, p=0.5, r=5)
mean = binomial_mean(10, 0.5)
c = combination(10, 5)
```

## 📝 Output Example

```
════════════════════════════════════════════════════════════
  PROBABILITY TOOLKIT  —  Permutation, Combination & Binomial
════════════════════════════════════════════════════════════

  FEATURES OF A BINOMIAL EXPERIMENT
  ────────────────────────────────────────────────────────────
  1. Fixed number of trials (n), each identical and independent.
  2. Each trial has exactly two outcomes: success or failure.
  3. Probability of success (p) is constant across all trials.
  4. Trials are mutually independent of each other.
  5. Random variable X counts total successes in n trials.
  6. X ~ B(n, p) → PMF: P(X=r) = C(n,r) · p^r · q^(n-r)

  Setup: X ~ B(5, 0.5)   q = 0.5000
  Mean (μ)           = n·p        = 5·0.5 = 2.5000
  Variance (σ²)      = n·p·q      = 5·0.5·0.5 = 1.2500
  Std deviation (σ)  = √(n·p·q)   = √1.2500 = 1.1180
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Enhancement

- Graphical visualization of distributions (matplotlib/seaborn)
- Web interface (Flask/Streamlit)
- Approximation methods (normal approximation to binomial)
- Negative binomial distribution support
- Interactive plotting of PMF and CDF
- Confidence interval calculations

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as an educational tool for probability and statistics calculations.

## 🙋 Support

For issues, questions, or suggestions, please open an issue on GitHub or contact the project maintainer.

---

**Last Updated:** 2026  
**Version:** 1.0.0
