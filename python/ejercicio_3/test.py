import unittest
from main import find_missing_letter


class TestFindMissingLetter(unittest.TestCase):
    def test_basic_cases(self):
        """
        Find_missing_letter tests
        """
        self.assertEqual(find_missing_letter(["a", "b", "c", "d", "f"]), "e")
        self.assertEqual(find_missing_letter(["O", "Q", "R", "S"]), "P")

    def test_result_false(self):
        """
        Tests with results in false
        """
        self.assertEqual(find_missing_letter(['O', 'P', 'Q', 'R']), False)
        self.assertEqual(find_missing_letter(['E']), False)
        self.assertEqual(find_missing_letter(['a', '$', 'c', 'd', 'f']), False)
        self.assertEqual(find_missing_letter(['a', 'B', 'c', 'd', 'f']), False)
        self.assertEqual(find_missing_letter(['A', 'z', 'R', 'Q', 'I']), False)


if __name__ == "__main__":
    unittest.main()
