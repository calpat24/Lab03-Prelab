import unittest
from q2 import bisection_root, polynomial


class TestBisectionMethod(unittest.TestCase):
    def test_root_exists(self):
        root = bisection_root(-2, 2)
        self.assertIsNotNone(root, "The root should not be None")

    def test_root_accuracy(self):
        root = bisection_root(-2, 2)
        self.assertAlmostEqual(polynomial(root), 0, places=3,
                               msg="The polynomial value at the root should be close to 0")

    def test_invalid_range_assertion(self):
        with self.assertRaises(AssertionError, msg="An AssertionError should be raised for an invalid range"):
            bisection_root(5, 3)

    def test_no_sign_change_assertion(self):
        with self.assertRaises(AssertionError,
                               msg="An AssertionError should be raised when there is no sign change across the interval"):
            bisection_root(0, 2)  # No root exists in this interval for the given polynomial


if __name__ == "__main__":
    unittest.main()
