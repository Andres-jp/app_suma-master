import unittest
from calc import rest_two, sum_two

class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_two(2, 3), 5.0)
        self.assertAlmostEqual(sum_two("1.5", "2.5"), 4.0)

    def test_error(self):
        with self.assertRaises(ValueError):
            sum_two("a", 3)

    def test_rest(self):
        self.assertEqual(rest_two(2, 3), -1.0)
        self.assertAlmostEqual(rest_two("1.5", "2.5"), -1.0)

    def test_error(self):
        with self.assertRaises(ValueError):
            rest_two("a", 3)
if __name__ == '__main__':
    unittest.main()
