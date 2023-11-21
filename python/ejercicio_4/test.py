import unittest
from main import array_diff


class TestArrayDiff(unittest.TestCase):
    def test_basic_case(self):
        """
        Basic Test Cases
        """
        self.assertEqual(array_diff([1, 2], [1]), [2])
        self.assertEqual(array_diff([1, 2, 2], [1]), [2, 2])
        self.assertEqual(array_diff([1, 2, 2], [2]), [1])
        self.assertEqual(array_diff([1, 2, 2], []), [1, 2, 2])
        self.assertEqual(array_diff([], [1, 2]), [])
        self.assertEqual(array_diff([1, 2, 3], [1, 2]), [3])


if __name__ == "__main__":
    unittest.main()
