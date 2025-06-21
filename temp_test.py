#!/usr/bin/env python3
"""
ai-test-project Test Suite
"""

import unittest
from main import Ai_Test_ProjectAI

class TestAi_Test_Project(unittest.TestCase):
    
    def setUp(self):
        self.ai = Ai_Test_ProjectAI()
    
    def test_model_loading(self):
        """Model yükleme testi"""
        self.assertIsNotNone(self.ai.model)
    
    def test_text_processing(self):
        """Metin işleme testi"""
        result = self.ai.process("Test input")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()
