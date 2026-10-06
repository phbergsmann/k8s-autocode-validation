import unittest

from calculator import weighted_average


class WeightedAverageTest(unittest.TestCase):
    def test_unequal_weights_divides_by_sum_of_weights(self):
        # (1*1 + 2*3) / (1 + 3) == 1.75; the old code returned 5/2 == 2.5
        self.assertEqual(weighted_average([1, 2], [1, 3]), 1.75)

    def test_zero_weight_among_positive_weights_is_allowed(self):
        # Zero weight contributes nothing; result must use the positive sum.
        self.assertEqual(weighted_average([10, 3], [0, 2]), 3.0)

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1, -1])

    def test_zero_total_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [0, 0])


if __name__ == "__main__":
    unittest.main()
