import unittest

from calculator import weighted_average


class WeightedAverageTest(unittest.TestCase):
    def test_unequal_weights(self):
        # weights [1, 2, 3] -> weighted sum = 1*1 + 2*2 + 3*3 = 14
        # correct divisor is sum(weights) = 6, so expected is 14/6 = 7/3
        # the old bug divided by len(values) == 3, giving 14/3 (wrong)
        values = [1, 2, 3]
        weights = [1, 2, 3]
        self.assertAlmostEqual(weighted_average(values, weights), 14 / 6)

    def test_unequal_weights_non_uniform(self):
        # distinct, non-uniform weights to catch divisor mistakes
        values = [10, 20, 30]
        weights = [1, 3, 5]
        # weighted sum = 10*1 + 20*3 + 30*5 = 10 + 60 + 150 = 220
        # sum(weights) = 9 -> 220/9
        self.assertAlmostEqual(weighted_average(values, weights), 220 / 9)

    def test_equal_weights_matches_simple_mean(self):
        values = [4, 8, 12]
        weights = [1, 1, 1]
        self.assertAlmostEqual(weighted_average(values, weights), 8.0)

    def test_rejects_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1])

    def test_rejects_negative_weights(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1, -1])

    def test_rejects_zero_total_weight(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [0, 0])


if __name__ == "__main__":
    unittest.main()
