# test_fastifynode.py
"""
Tests for FastifyNode module.
"""

import unittest
from fastifynode import FastifyNode

class TestFastifyNode(unittest.TestCase):
    """Test cases for FastifyNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FastifyNode()
        self.assertIsInstance(instance, FastifyNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FastifyNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
