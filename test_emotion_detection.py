"""
Unit Tests for Emotion Detection Application
This module contains test cases for the emotion detection functionality.
"""

import unittest
from emotion_detection import emotion_predictor, emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotion detection functions.
    """
    
    def test_emotion_predictor_joy(self):
        """
        Test emotion prediction for a joyful statement.
        """
        result = emotion_predictor("I am so happy today!")
        self.assertIsNotNone(result)
        self.assertIn('joy', result)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_predictor_anger(self):
        """
        Test emotion prediction for an angry statement.
        """
        result = emotion_predictor("I am really mad about this!")
        self.assertIsNotNone(result)
        self.assertIn('anger', result)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_predictor_sadness(self):
        """
        Test emotion prediction for a sad statement.
        """
        result = emotion_predictor("I feel so sad and lonely.")
        self.assertIsNotNone(result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_predictor_fear(self):
        """
        Test emotion prediction for a fearful statement.
        """
        result = emotion_predictor("I am scared of what might happen.")
        self.assertIsNotNone(result)
        self.assertIn('fear', result)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_predictor_empty_string(self):
        """
        Test emotion prediction with empty string.
        Should return an error.
        """
        result = emotion_predictor("")
        self.assertIsNotNone(result)
        self.assertIn('error', result)
    
    def test_emotion_predictor_none(self):
        """
        Test emotion prediction with None input.
        Should return an error.
        """
        result = emotion_predictor(None)
        self.assertIsNotNone(result)
        self.assertIn('error', result)
    
    def test_emotion_predictor_response_structure(self):
        """
        Test that the response has the correct structure.
        """
        result = emotion_predictor("This is a test statement.")
        self.assertIsInstance(result, dict)
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_detector_function_exists(self):
        """
        Test that emotion_detector function exists and is callable.
        """
        self.assertTrue(callable(emotion_detector))
    
    def test_emotion_predictor_function_exists(self):
        """
        Test that emotion_predictor function exists and is callable.
        """
        self.assertTrue(callable(emotion_predictor))


if __name__ == '__main__':
    unittest.main()

