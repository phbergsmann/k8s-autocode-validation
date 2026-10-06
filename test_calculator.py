import unittest

from calculator import weighted_average


class WeightedAverageTest(unittest.TestCase):
    def test_unequal_weights_divides_by_sum_of_weights(self):
        # (1*1 + 2*3) / (1 + 3) = 7/4 = 1.75;
        # dividing by count (5/2) would give the wrong value 2.5.
        self.assertAlmostEqual(weighted_average([1, 2], [1, 3]), 1.75)

    def test_zero_weight_contributes_nothing(self):
        # (5*0 + 10*2) / (0 + 2) = 10; the zero-weight value must be ignored.
        self.assertAlmostEqual(weighted_average([5, 10], [0, 2]), 10.0)

    def test_validation_unchanged(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1])
        with self.assertRaises(ValueError):
            weighted_average([], [])
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [-1, 3])
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [0, 0])


if __name__ == "__main__":
    unittest.main()
