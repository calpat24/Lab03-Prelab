
# COMP100 2025F Lab 03: Guess-Check, Approximation, Bisection - PreLab

## Deadline: 10:00 AM Friday 7th November 2025

The test cases given are just sample tests, and additional test cases may be used while grading.

# Question 1: Solving Exponential Equations (40 Points)

### Objective
Develop a function named `iterative_approximation_exponential` to approximate the solution to exponential equations of the form `a^x = b`, using iterative methods without relying on direct logarithmic computation.

#### Inputs
- `a` (float): Base of the exponential equation, where `a > 0` and `a` is not equal to 1.
- `b` (float): Result of the exponential equation, where `b > 0`.
- `epsilon` (float, optional): Tolerance for the approximation, a small positive number that defines the acceptable difference between `a^x` and `b`. Default: `0.001`.
- `delta` (float, optional): Incremental step for `x` in each iteration, a small positive number used to refine the approximation of `x`. Default: `0.0001`.
- `max_iterations` (int, optional): The maximum number of iterations to attempt before stopping the approximation process. Default: `100000`

### Output
- `x` (float): The approximated value of `x` that solves `a^x = b`.

### Method
- Start with an initial guess for `x`,  must be 0.
- Increment `x` by a small value, `delta`, in each iteration to refine the approximation.
- Continue calculating `a^x` each iteration until the absolute value of `a^x - b` is less than `epsilon` or a maximum number of iterations is reached, to avoid infinite loops.
- If the loop exceeds the maximum number of iterations without finding a solution that meets the tolerance, print the string "Solution not found within max iterations" and return `None`.

### Examples
#### Example 1 (Basic Case)
```python
iterative_approximation_exponential(a=2, b=8)
```
**Expected Output:** `x ≈ 3.0`
_(Since `2^3 = 8`, the approximation should return a value close to `3.0`.)_

#### Example 2 (Non-Integer x)
```python
iterative_approximation_exponential(a=3, b=10)
```
**Expected Output:** `x ≈ 2.1`
_(Since `3^2.1 ≈ 10`, the function should approximate `x` correctly.)_

#### Example 3 (No solution within max iterations)
```python
iterative_approximation_exponential(a=5, b=1e20, max_iterations=1000)
```
**Expected Output:** `"Solution not found within max iterations"`
_(If the solution requires a very large `x`, the function should terminate early.)_

## Question 2: Root Finding for Quadratic Polynomials Using Bisection (60 Points)

### Objective
Implement a function named `bisection_root` that uses the bisection method to approximate a root of the quadratic polynomial `3x^2 - 4x - 5 = 0` within a specified interval. This method demonstrates a numerical technique for finding roots of polynomial equations when analytical solutions are difficult to obtain or require simplification.

### Inputs
- Interval `[a, b]`: The range within which to search for the root.
- `epsilon` (float, optional): The precision level for the approximation. It indicates the threshold at which the absolute value of the polynomial function evaluated at the root approximation is considered sufficiently close to 0. Default: `0.0001`.

### Output
- Root approximation (float): The estimated value of the root, found within the given tolerance.

### Method
- The `bisection_root` function requires the interval `[a, b]` to contain at least one root. For a root to be present within `[a, b]`, the function must change signs at the endpoints of the interval, which implies `f(a) * f(b) < 0`. This condition guarantees that one end of the range is below 0 and the other is above 0, indicating a zero-crossing or a root within the interval.
- Calculate the midpoint `m` of the interval as `(a + b) / 2`.
- Determine which subinterval, `[a, m]` or `[m, b]`, contains the root by evaluating the sign of the product `f(a) * f(m)`. If the product is negative, the root lies within `[a, m]`; otherwise, it is within `[m, b]`.
- Repeat the bisection process on the selected subinterval, recalculating the midpoint for the new interval in each iteration.
- Continue this iterative process until the absolute value of the polynomial evaluated at the midpoint, `abs(f(m))`, is less than the specified `epsilon`. This condition indicates that the midpoint `m` is an approximation of the root that meets the desired precision level.

### Examples
#### Example 1
```python
bisection_root(a=-3, b=2)
```
**Expected Output:** `x ≈ -0.786`
_(Since one of the roots of `3x^2 - 4x - 5 = 0` is around `-0.786`.)_

#### Example 2
```python
bisection_root(a=1, b=4)
```
**Expected Output:** `x ≈ 2.119`
_(Since one of the roots of `3x^2 - 4x - 5 = 0` is around `2.119`.)_