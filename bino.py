from math import gcd, sqrt, factorial


# ── helpers ──────────────────────────────────────────────────────────────────

def combination(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutation(n, r):
    if r > n or r < 0:
        return 0
    result = 1
    for i in range(r):
        result *= (n - i)
    return result

def combination_fraction(n, r):
    if r > n or r < 0:
        return (0, 1)
    r = min(r, n - r)
    num, den = 1, 1
    for i in range(r):
        num *= (n - i)
        den *= (i + 1)
    g = gcd(num, den)
    return (num // g, den // g)

def pmf(n, p, r):
    """P(X = r) for X ~ B(n, p)"""
    return combination(n, r) * (p ** r) * ((1 - p) ** (n - r))


# ── binomial stats ────────────────────────────────────────────────────────────

def binomial_mean(n, p):
    return n * p

def binomial_variance(n, p):
    return n * p * (1 - p)

def binomial_std(n, p):
    return sqrt(binomial_variance(n, p))


# ── probability queries ───────────────────────────────────────────────────────

def prob_exact(n, p, r):
    """P(X = r)"""
    return pmf(n, p, r)

def prob_at_most(n, p, r):
    """P(X <= r)"""
    return sum(pmf(n, p, i) for i in range(r + 1))

def prob_at_least(n, p, r):
    """P(X >= r)"""
    return sum(pmf(n, p, i) for i in range(r, n + 1))

def prob_between(n, p, r1, r2):
    """P(r1 <= X <= r2)"""
    lo, hi = min(r1, r2), max(r1, r2)
    return sum(pmf(n, p, i) for i in range(lo, hi + 1))


# ── display helpers ───────────────────────────────────────────────────────────

def print_separator(char="─", width=60):
    print(char * width)

def print_distribution(n, p):
    print("\n  r   C(n,r)       P(X=r)      P(X<=r)")
    print("  " + "─" * 45)
    cumulative = 0
    for r in range(n + 1):
        c = combination(n, r)
        prob = pmf(n, p, r)
        cumulative += prob
        print(f"  {r:2d}   {c:6d}    {prob:10.6f}    {min(cumulative, 1):.6f}")

def print_features():
    print_separator()
    print("  FEATURES OF A BINOMIAL EXPERIMENT")
    print_separator()
    features = [
        "Fixed number of trials (n), each identical and independent.",
        "Each trial has exactly two outcomes: success or failure.",
        "Probability of success (p) is constant across all trials.",
        "Trials are mutually independent of each other.",
        "Random variable X counts total successes in n trials.",
        "X ~ B(n, p)  →  PMF: P(X=r) = C(n,r) · p^r · q^(n-r)",
    ]
    for i, f in enumerate(features, 1):
        print(f"  {i}. {f}")
    print()

def print_stats(n, p, label=""):
    q = 1 - p
    mu  = binomial_mean(n, p)
    var = binomial_variance(n, p)
    sd  = binomial_std(n, p)
    if label:
        print(f"\n  [{label}]")
    print(f"  Mean (μ)           = n·p        = {n}·{p} = {mu:.4f}")
    print(f"  Variance (σ²)      = n·p·q      = {n}·{p}·{q:.4f} = {var:.4f}")
    print(f"  Std deviation (σ)  = √(n·p·q)   = √{var:.4f} = {sd:.4f}")


# ── perm / comb display ───────────────────────────────────────────────────────

def show_perm_comb(n, r):
    print_separator()
    print("  PERMUTATION & COMBINATION")
    print_separator()
    perm = permutation(n, r)
    num, den = combination_fraction(n, r)
    comb_val = num // den if den == 1 else None
    print(f"  P({n},{r}) = {perm}")
    if den == 1:
        print(f"  C({n},{r}) = {num}  (already an integer)")
    else:
        print(f"  C({n},{r}) = {num}/{den}  (= {num//den})")
    print()


# ── main menu ─────────────────────────────────────────────────────────────────

def get_int(prompt, lo=None, hi=None):
    while True:
        try:
            val = int(input(prompt))
            if lo is not None and val < lo:
                print(f"  Must be >= {lo}"); continue
            if hi is not None and val > hi:
                print(f"  Must be <= {hi}"); continue
            return val
        except ValueError:
            print("  Please enter a valid integer.")

def get_float(prompt, lo=0.0, hi=1.0):
    while True:
        try:
            val = float(input(prompt))
            if not (lo <= val <= hi):
                print(f"  Must be between {lo} and {hi}"); continue
            return val
        except ValueError:
            print("  Please enter a valid number.")

def binomial_menu():
    print_separator()
    print("  BINOMIAL EXPERIMENT SOLVER")
    print_separator()
    n = get_int("  Enter number of trials (n): ", lo=1)
    p = get_float("  Enter probability of success (p, 0–1): ")
    q = 1 - p

    print(f"\n  Setup: X ~ B({n}, {p})   q = {q:.4f}")
    print_stats(n, p)

    print("\n  Query type:")
    print("   1. Exactly r successes       P(X = r)")
    print("   2. At most r successes       P(X <= r)")
    print("   3. At least r successes      P(X >= r)")
    print("   4. Between r1 and r2         P(r1 <= X <= r2)")
    print("   5. Full distribution table")
    choice = get_int("  Select (1-5): ", lo=1, hi=5)

    print()
    if choice == 1:
        r = get_int(f"  Enter r (0–{n}): ", lo=0, hi=n)
        prob = prob_exact(n, p, r)
        c = combination(n, r)
        print(f"\n  P(X = {r}) = C({n},{r}) · {p}^{r} · {q:.4f}^{n-r}")
        print(f"           = {c} · {p**r:.6f} · {q**(n-r):.6f}")
        print(f"           = {prob:.6f}  ≈  {prob*100:.2f}%")
        print_stats(n, p, f"P(X = {r})")

    elif choice == 2:
        r = get_int(f"  Enter r (0–{n}): ", lo=0, hi=n)
        print(f"\n  P(X <= {r}) = Σ P(X=i) for i = 0..{r}")
        total = 0
        for i in range(r + 1):
            pi = pmf(n, p, i)
            total += pi
            print(f"    P(X={i}) = {pi:.6f}")
        print(f"  ─────────────────────────")
        print(f"  P(X <= {r}) = {total:.6f}  ≈  {total*100:.2f}%")
        print_stats(n, p, f"P(X ≤ {r})")

    elif choice == 3:
        r = get_int(f"  Enter r (0–{n}): ", lo=0, hi=n)
        print(f"\n  P(X >= {r}) = Σ P(X=i) for i = {r}..{n}")
        total = 0
        for i in range(r, n + 1):
            pi = pmf(n, p, i)
            total += pi
            print(f"    P(X={i}) = {pi:.6f}")
        print(f"  ─────────────────────────")
        print(f"  P(X >= {r}) = {total:.6f}  ≈  {total*100:.2f}%")
        print_stats(n, p, f"P(X ≥ {r})")

    elif choice == 4:
        r1 = get_int(f"  Enter r1 (0–{n}): ", lo=0, hi=n)
        r2 = get_int(f"  Enter r2 ({r1}–{n}): ", lo=r1, hi=n)
        print(f"\n  P({r1} <= X <= {r2}) = Σ P(X=i) for i = {r1}..{r2}")
        total = 0
        for i in range(r1, r2 + 1):
            pi = pmf(n, p, i)
            total += pi
            print(f"    P(X={i}) = {pi:.6f}")
        print(f"  ─────────────────────────")
        print(f"  P({r1} <= X <= {r2}) = {total:.6f}  ≈  {total*100:.2f}%")
        print_stats(n, p, f"P({r1} ≤ X ≤ {r2})")

    else:
        print_distribution(n, p)
        print_stats(n, p)


def main():
    print("\n" + "═" * 60)
    print("  PROBABILITY TOOLKIT  —  Permutation, Combination & Binomial")
    print("═" * 60)

    print_features()

    print("  MAIN MENU")
    print_separator()
    print("   1. Permutation & Combination (P and C)")
    print("   2. Binomial Experiment Solver")
    choice = get_int("  Select (1-2): ", lo=1, hi=2)

    if choice == 1:
        n = get_int("\n  Enter n: ", lo=0)
        r = get_int("  Enter r: ", lo=0)
        if r > n:
            print("  Error: r must be <= n"); return
        show_perm_comb(n, r)

    elif choice == 2:
        binomial_menu()

    print()
    print_separator()
    print("  Done.")
    print_separator()


if __name__ == "__main__":
    main()