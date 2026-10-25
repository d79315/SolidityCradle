# test_soliditycradle.py
"""
Tests for SolidityCradle module.
"""

import unittest
from soliditycradle import SolidityCradle

class TestSolidityCradle(unittest.TestCase):
    """Test cases for SolidityCradle class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityCradle()
        self.assertIsInstance(instance, SolidityCradle)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityCradle()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
