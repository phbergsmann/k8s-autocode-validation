import unittest

from calculator import weighted_average


class WeightedAverageTests(unittest.TestCase):
    def test_unequal_weights(self):
        # (1*1 + 2*2 + 3*3) / (1+2+3) = 14/6
        self.assertAlmostEqual(
            weighted_average([1, 2, 3], [1, 2, 3]), 14 / 6
        )

    def test_zero_weight_with_positive_weights(self):
        # Zero-weighted value contributes nothing; total = 5
        self.assertEqual(weighted_average([10, 20], [0, 5]), 20)
        # Order-independent: leading zero weight behaves the same
        self.assertEqual(weighted_average([10, 20], [5, 0]), 10)

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
