import unittest

from calculator import weighted_average


class WeightedAverageTest(unittest.TestCase):
    def test_unequal_weights_divides_by_sum_of_weights(self):
        # (10*1 + 20*2) / (1 + 2) = 50 / 3
        result = weighted_average([10, 20], [1, 2])
        self.assertAlmostEqual(result, 50 / 3)

    def test_zero_weights_alongside_positive_weights(self):
        # Zero weights are valid; the result is driven by the positive ones.
        # (5*0 + 10*2) / (0 + 2) = 10
        result = weighted_average([5, 10], [0, 2])
        self.assertAlmostEqual(result, 10.0)

    def test_negative_weights_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1, -1])

    def test_zero_total_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [0, 0])

    def test_length_mismatch_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1])

    def test_empty_inputs_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([], [])


if __name__ == "__main__":
    unittest.main()
