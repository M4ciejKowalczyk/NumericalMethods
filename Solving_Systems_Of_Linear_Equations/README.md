# Systems of Linear Equations: Iterative vs. Direct Solvers

## Overview
This project explores and implements numerical methods for solving systems of linear equations (`Ax = b`). Such systems frequently arise from the discretization of differential equations in fields like fluid dynamics, electronics, and structural mechanics. Developed from scratch in Python, the project compares two iterative algorithms (Jacobi, Gauss-Seidel) and one direct algorithm (LU Factorization), analyzing their convergence, reliability, and computational complexity on banded matrices.

## Features & Implemented Algorithms
* **Iterative Methods (Jacobi & Gauss-Seidel):** Custom implementations that approximate the solution by updating the vectors iteratively. The convergence is dynamically monitored using the Euclidean norm of the residual vector (`r = Ax - b`), terminating when the error falls below a $10^{-9}$ threshold.
* **Direct Method (LU Factorization):** A custom algorithm that decomposes the system matrix into lower (L) and upper (U) triangular matrices, followed by forward and backward substitution to guarantee a precise solution.
* **Performance Benchmarking:** Automated testing and visualization of execution time and iteration counts across varying matrix sizes (from N=100 up to N=3000).

## Technologies
* **Language:** Python
* **Libraries:** `numpy` (for high-performance matrix operations), `matplotlib` (for generating logarithmic and linear convergence/time charts)

## Key Findings
Through extensive testing on different matrix configurations, the project demonstrates that:
1. **Convergence Speed:** For strictly diagonally dominant matrices, the Gauss-Seidel method converges significantly faster (e.g., 28 iterations vs. 46 iterations for Jacobi) and requires less computational time.
2. **Reliability vs. Divergence:** When the matrix loses strong diagonal dominance (e.g., changing the main diagonal value from 7 to 3), both iterative methods fail and diverge dramatically (residual norm approaches infinity). In contrast, the direct LU Factorization method successfully solves the system.
3. **Time Complexity:** Iterative methods scale much better for large matrices with an estimated complexity of $O(n^2)$. LU Factorization scales poorly at $O(n^3)$, making it computationally expensive for massive datasets, but it remains the necessary fallback when iterative methods lack guaranteed convergence.

## How to Run
1. Ensure Python is installed with the `numpy` and `matplotlib` packages.
2. Run `main.py` to execute the simulations. The script will generate the banded matrices, run all three solving methods, and display charts illustrating residual norm convergence and execution times.
