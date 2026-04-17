# test_nervosckb.py
"""
Tests for NervosCKB module.
"""

import unittest
from nervosckb import NervosCKB

class TestNervosCKB(unittest.TestCase):
    """Test cases for NervosCKB class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NervosCKB()
        self.assertIsInstance(instance, NervosCKB)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NervosCKB()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
