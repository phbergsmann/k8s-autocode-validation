import unittest

from calculator import weighted_average


class WeightedAverageTest(unittest.TestCase):
    def test_unequal_weights_divides_by_sum_of_weights(self):
        # (1*1 + 2*3) / (1+3) = 7/4; old len(values) denominator gave 3.5
        self.assertAlmostEqual(weighted_average([1, 2], [1, 3]), 1.75)

    def test_equal_weights_match_plain_average(self):
        self.assertAlmostEqual(weighted_average([2, 4, 6], [1, 1, 1]), 4.0)

    def test_single_value_with_non_unit_weight(self):
        self.assertAlmostEqual(weighted_average([5], [2]), 5.0)

    def test_mismatched_lengths_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1])

    def test_empty_inputs_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([], [])

    def test_nonpositive_total_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [0, 0])

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1, -1])


if __name__ == "__main__":
    unittest.main()
