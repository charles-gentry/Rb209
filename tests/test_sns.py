"""Tests for SNS calculation."""

import unittest

from rb209.engine import calculate_sns


class TestSNS(unittest.TestCase):
    def test_cereals_light_high_rainfall(self):
        result = calculate_sns("cereals", "light", "high")
        self.assertEqual(result.sns_index, 0)

    def test_cereals_medium_medium_rainfall(self):
        result = calculate_sns("cereals", "medium", "medium")
        self.assertEqual(result.sns_index, 1)

    def test_cereals_heavy_low_rainfall(self):
        result = calculate_sns("cereals", "heavy", "low")
        self.assertEqual(result.sns_index, 2)

    def test_oilseed_rape_medium_medium(self):
        result = calculate_sns("oilseed-rape", "medium", "medium")
        self.assertEqual(result.sns_index, 2)

    def test_peas_beans_heavy_low(self):
        result = calculate_sns("peas-beans", "heavy", "low")
        self.assertEqual(result.sns_index, 4)

    def test_long_term_grass_organic_low(self):
        result = calculate_sns("grass-long-term", "organic", "low")
        self.assertEqual(result.sns_index, 6)

    def test_long_term_grass_light_low(self):
        result = calculate_sns("grass-long-term", "light", "low")
        self.assertEqual(result.sns_index, 4)

    def test_method_is_field_assessment(self):
        result = calculate_sns("cereals", "medium", "medium")
        self.assertEqual(result.method, "field-assessment")

    def test_notes_contain_residue_category(self):
        result = calculate_sns("cereals", "medium", "medium")
        self.assertTrue(any("low" in n.lower() for n in result.notes))

    def test_invalid_previous_crop_raises(self):
        with self.assertRaises(ValueError):
            calculate_sns("bananas", "medium", "medium")

    def test_invalid_soil_type_raises(self):
        with self.assertRaises(ValueError):
            calculate_sns("cereals", "volcanic", "medium")

    def test_invalid_rainfall_raises(self):
        with self.assertRaises(ValueError):
            calculate_sns("cereals", "medium", "extreme")


if __name__ == "__main__":
    unittest.main()
