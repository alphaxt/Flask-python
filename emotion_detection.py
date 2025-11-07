"""
Emotion Detection Module
This module provides functionality to detect emotions in text using Watson NLP.
"""

import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions


def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson Natural Language Understanding.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: A dictionary containing emotion scores and dominant emotion
              Format: {
                  'anger': float,
                  'disgust': float,
                  'fear': float,
                  'joy': float,
                  'sadness': float,
                  'dominant_emotion': str
              }
    """
    # Watson NLU API credentials from environment variables
    url = os.getenv('WATSON_NLU_URL', 
                    "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID")
    apikey = os.getenv('WATSON_NLU_APIKEY', "YOUR_API_KEY")
    
    # Check if using placeholder credentials (for testing/development)
    if apikey == "YOUR_API_KEY" or url.endswith("YOUR_INSTANCE_ID"):
        # Return mock response for testing
        return _mock_emotion_detection(text_to_analyze)
    
    # Initialize authenticator
    try:
        authenticator = IAMAuthenticator(apikey)
        
        # Initialize Natural Language Understanding service
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2021-08-01',
            authenticator=authenticator
        )
        
        natural_language_understanding.set_service_url(url)
        
        # Analyze emotions
        response = natural_language_understanding.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        
        # Extract emotion scores
        emotions = response['emotion']['document']['emotion']
        
        # Format the response
        formatted_response = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0)
        }
        
        # Find dominant emotion
        dominant_emotion = max(formatted_response.items(), key=lambda x: x[1])[0]
        formatted_response['dominant_emotion'] = dominant_emotion
        
        return formatted_response
        
    except Exception as e:
        # Return error response
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': str(e)
        }


def _mock_emotion_detection(text_to_analyze):
    """
    Mock emotion detection for testing purposes.
    Provides basic emotion analysis based on keyword matching.
    
    Args:
        text_to_analyze (str): The text to analyze
        
    Returns:
        dict: Mock emotion scores
    """
    text_lower = text_to_analyze.lower()
    
    # Simple keyword-based emotion detection for testing
    joy_keywords = ['happy', 'joy', 'excited', 'great', 'wonderful', 'amazing', 'love', 'fantastic']
    anger_keywords = ['angry', 'mad', 'furious', 'annoyed', 'frustrated', 'hate']
    sadness_keywords = ['sad', 'depressed', 'lonely', 'unhappy', 'miserable', 'cry']
    fear_keywords = ['scared', 'afraid', 'fear', 'worried', 'anxious', 'nervous']
    disgust_keywords = ['disgust', 'disgusted', 'revolting', 'gross', 'nasty']
    
    # Count keyword matches
    joy_score = sum(1 for word in joy_keywords if word in text_lower) * 0.3
    anger_score = sum(1 for word in anger_keywords if word in text_lower) * 0.3
    sadness_score = sum(1 for word in sadness_keywords if word in text_lower) * 0.3
    fear_score = sum(1 for word in fear_keywords if word in text_lower) * 0.3
    disgust_score = sum(1 for word in disgust_keywords if word in text_lower) * 0.3
    
    # Normalize scores (ensure they sum to a reasonable value)
    total = joy_score + anger_score + sadness_score + fear_score + disgust_score
    if total == 0:
        # Default to neutral (slight joy)
        joy_score = 0.4
        anger_score = 0.1
        sadness_score = 0.1
        fear_score = 0.1
        disgust_score = 0.1
    else:
        # Normalize to sum to 1.0
        factor = 1.0 / total
        joy_score *= factor
        anger_score *= factor
        sadness_score *= factor
        fear_score *= factor
        disgust_score *= factor
    
    formatted_response = {
        'anger': min(anger_score, 1.0),
        'disgust': min(disgust_score, 1.0),
        'fear': min(fear_score, 1.0),
        'joy': min(joy_score, 1.0),
        'sadness': min(sadness_score, 1.0)
    }
    
    # Find dominant emotion
    dominant_emotion = max(formatted_response.items(), key=lambda x: x[1])[0]
    formatted_response['dominant_emotion'] = dominant_emotion
    
    return formatted_response


def emotion_predictor(text_to_analyze):
    """
    Predicts emotions in text and returns formatted output.
    This is a wrapper function that formats the output for display.
    
    Args:
        text_to_analyze (str): The text to analyze
        
    Returns:
        dict: Formatted emotion analysis results
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'error': 'Invalid text! Please try again.'
        }
    
    result = emotion_detector(text_to_analyze)
    
    # Format percentages for display
    if 'error' not in result:
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
            if result[emotion] is not None:
                result[emotion] = round(result[emotion] * 100, 2)
    
    return result

