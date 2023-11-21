import unittest
from main import validate_pin


class TestPin(unittest.TestCase):
    def test_pin_length(self):
        """
        Should return False for pins with length other than 4 or 6.
        """
        self.assertEqual(validate_pin("1"), False)
        self.assertEqual(validate_pin("12"), False)
        self.assertEqual(validate_pin("123"), False)
        self.assertEqual(validate_pin("12345"), False)
        self.assertEqual(validate_pin("1234567"), False)
        self.assertEqual(validate_pin("-1234"), False)
        self.assertEqual(validate_pin("-12345"), False)
        self.assertEqual(validate_pin("1.234"), False)
        self.assertEqual(validate_pin("00000000"), False)

    def test_pin_char(self):
        """
        Should return False for pins which contain characters other
         than digits
        """
        self.assertEqual(validate_pin("a234"), False)
        self.assertEqual(validate_pin(".234"), False)

    def test_valid_pin(self):
        """
        Should return True for valid pins
        """
        self.assertEqual(validate_pin("1234"), True)
        self.assertEqual(validate_pin("0000"), True)
        self.assertEqual(validate_pin("1111"), True)
        self.assertEqual(validate_pin("123456"), True)
        self.assertEqual(validate_pin("098765"), True)
        self.assertEqual(validate_pin("000000"), True)
        self.assertEqual(validate_pin("123456"), True)
        self.assertEqual(validate_pin("090909"), True)


if __name__ == "__main__":
    unittest.main()
