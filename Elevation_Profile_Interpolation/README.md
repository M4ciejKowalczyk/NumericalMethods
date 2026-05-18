# Elevation Profile Approximation: Interpolation Methods

## Overview
This project evaluates the performance of different numerical interpolation methods for reconstructing the elevation profiles of cycling and running routes. By sampling elevation data at specific node points, the project reconstructs the continuous route profile using algorithms implemented entirely from scratch in Python. The core analysis focuses on comparing the classical **Lagrange Polynomial Interpolation** against **Cubic Spline Interpolation**.

## Features
* **Lagrange Polynomial Interpolation:** Evaluates the route by constructing an $n-1$ degree polynomial passing through all given nodes. Includes a normalization step scaling the domain to `[0, 1]` to enhance numerical stability. 
* **Cubic Splines:** Implements piece-wise 3rd-degree polynomials (natural splines) ensuring continuous first and second derivatives across all nodes, guaranteeing a smooth curve.
* **Runge's Phenomenon Mitigation:** Explores the impact of node placement. The project tests both uniformly distributed nodes and **Chebyshev nodes** (where points are denser at the edges of the interval) to control the violent oscillations characteristic of polynomial interpolation at higher degrees.
* **Real-World Data Testing:** Evaluates the algorithms on actual GPS `.csv` data, representing two distinct route types:
    * `GlebiaChallenge.csv`: A smooth route with one distinct, gentle valley.
    * `Unsyncable_ride.csv`: A chaotic route with numerous rapid, sharp elevation changes.

## Technologies
* **Language:** Python
* **Libraries:** `numpy` (for matrix operations), `pandas` (for data reading), `matplotlib` (for visual analysis).

## Key Findings
1. **The Flaws of Lagrange:** While simple, Lagrange interpolation suffers severely from Runge's phenomenon as the number of nodes increases (e.g., at 16 or 32 nodes), causing massive, unrealistic oscillations at the edges of the elevation profile.
2. **Chebyshev Nodes Help, but Have Limits:** Switching from uniform nodes to Chebyshev nodes significantly reduced edge oscillations in the Lagrange method. However, because Chebyshev nodes are sparse in the middle of the interval, the center of the route lost some detail compared to the uniform distribution.
3. **Splines are Superior:** Cubic splines provided the most robust and accurate approximation. They efficiently captured the general shape with as few as 8-16 nodes and remained numerically stable (no Runge's phenomenon) even at 32 nodes, accurately reconstructing even chaotic, rapidly changing elevation profiles. 

## How to Run
1. Ensure Python is installed with the necessary dependencies: `pandas`, `numpy`, and `matplotlib`.
2. Place your elevation `.csv` files inside a designated data folder.
3. Run `main.py` to process the data and generate comparison plots for the different interpolation techniques.
