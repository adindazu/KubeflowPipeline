# test_kubeflowpipeline.py
"""
Tests for KubeflowPipeline module.
"""

import unittest
from kubeflowpipeline import KubeflowPipeline

class TestKubeflowPipeline(unittest.TestCase):
    """Test cases for KubeflowPipeline class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KubeflowPipeline()
        self.assertIsInstance(instance, KubeflowPipeline)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KubeflowPipeline()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
