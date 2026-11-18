import unittest

from prepress import (
    TRIM_SIZES,
    gutter_inches,
    inner_margin_mm,
    spine_width_inches,
    trim_matches,
)


class SpineTests(unittest.TestCase):
    def test_known_value(self):
        self.assertAlmostEqual(spine_width_inches(300), 0.0186756, places=6)

    def test_thicker_stock_is_wider(self):
        self.assertGreater(
            spine_width_inches(400, "color-premium"),
            spine_width_inches(400, "black-white"),
        )

    def test_cover_adds_twice(self):
        a = spine_width_inches(200, cover_thickness_in=0.0)
        b = spine_width_inches(200, cover_thickness_in=0.01)
        self.assertAlmostEqual(b - a, 0.02, places=6)

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            spine_width_inches(0)
        with self.assertRaises(ValueError):
            spine_width_inches(100, "nope")


class GutterTests(unittest.TestCase):
    def test_bands(self):
        self.assertEqual(gutter_inches(150), 0.375)
        self.assertEqual(gutter_inches(151), 0.500)
        self.assertEqual(gutter_inches(828), 0.875)

    def test_over_maximum(self):
        with self.assertRaises(ValueError):
            gutter_inches(829)

    def test_margin_grows(self):
        self.assertGreater(inner_margin_mm(500), inner_margin_mm(200))


class TrimTests(unittest.TestCase):
    def test_a4_default_matches(self):
        self.assertTrue(trim_matches(8.27, 11.69, "a4"))

    def test_trade_size(self):
        self.assertTrue(trim_matches(6.0, 9.0, "6x9"))

    def test_mismatch(self):
        self.assertFalse(trim_matches(5.5, 8.25, "6x9"))

    def test_unknown_trim(self):
        with self.assertRaises(ValueError):
            trim_matches(6.0, 9.0, "nope")


if __name__ == "__main__":
    unittest.main()
