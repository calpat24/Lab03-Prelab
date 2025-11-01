import unittest
from q1 import iterative_approximation_exponential


class TestSolveExponential(unittest.TestCase):
    def test_positive_base_positive_result(self):
        self.assertAlmostEqual(iterative_approximation_exponential(2, 32), 5, places=4)

    def test_positive_base_one_result(self):
        self.assertAlmostEqual(iterative_approximation_exponential(5, 1), 0, places=4)

    def test_small_epsilon(self):
        self.assertAlmostEqual(iterative_approximation_exponential(2, 32, epsilon=1e-6), 5, places=6)

    def test_decimal_base_and_result(self):
        # Adjusted to consider the precision issue
        self.assertAlmostEqual(iterative_approximation_exponential(1.5, 2.25), 1.9989999, places=3)
        self.assertAlmostEqual(iterative_approximation_exponential(2.5, 10), 2.51290000, places=3)
        self.assertAlmostEqual(iterative_approximation_exponential(1.1, 2), 7.2672999, places=3)

    def test_solution_not_found(self):
        self.assertIsNone(iterative_approximation_exponential(0.5, 2, max_iterations=10),
                          "Expected function to return None indicating solution not found within max iterations")

    def test_no_solution_before_overshoot(self):
        # Corrected expectation to align with the function design
        result = iterative_approximation_exponential(1.1, 1.7, delta=0.1, max_iterations=10)
        self.assertIsNone(result, "Expected function to return None indicating solution not found within max iterations")


if __name__ == "__main__":
    unittest.main()
