import unittest

from calculator import weighted_average


class WeightedAverageTest(unittest.TestCase):
    def test_unequal_weights_divides_by_sum_of_weights(self):
        # values 1..3 with weights 1, 2, 3:
        # (1*1 + 2*2 + 3*3) / (1 + 2 + 3) = 14 / 6
        # The old code divided by len(values), giving 14 / 3 instead.
        result = weighted_average([1, 2, 3], [1, 2, 3])
        self.assertAlmostEqual(result, 14.0 / 6.0, places=9)

    def test_equal_weights_match_plain_average(self):
        result = weighted_average([2, 4, 6, 8], [1, 1, 1, 1])
        self.assertAlmostEqual(result, 5.0, places=9)

    def test_single_value(self):
        result = weighted_average([42], [7])
        self.assertAlmostEqual(result, 42.0, places=9)

    def test_mismatched_lengths_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1])

    def test_empty_inputs_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([], [])

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1, -1])

    def test_zero_total_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [0, 0])


if __name__ == "__main__":
    unittest.main()
