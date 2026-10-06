import unittest

from calculator import weighted_average


class WeightedAverageTest(unittest.TestCase):
    def test_unequal_weights(self):
        self.assertEqual(2.25, weighted_average([1, 2, 3], [1, 1, 2]))

    def test_equal_weights(self):
        self.assertEqual(2.0, weighted_average([1, 2, 3], [1, 1, 1]))

    def test_empty_inputs_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([], [])

    def test_mismatched_lengths_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [1])

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [-1, 1])

    def test_zero_total_weight_rejected(self):
        with self.assertRaises(ValueError):
            weighted_average([1, 2], [0, 0])


if __name__ == "__main__":
    unittest.main()
