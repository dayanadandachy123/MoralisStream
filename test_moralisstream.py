# test_moralisstream.py
"""
Tests for MoralisStream module.
"""

import unittest
from moralisstream import MoralisStream

class TestMoralisStream(unittest.TestCase):
    """Test cases for MoralisStream class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MoralisStream()
        self.assertIsInstance(instance, MoralisStream)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MoralisStream()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
