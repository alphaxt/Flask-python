"""
Flask Web Application Server for Emotion Detection
This is the main server file that handles web requests and serves the UI.
"""

from flask import Flask, render_template, request
from emotion_detection import emotion_predictor

app = Flask("Emotion Detection")

@app.route('/', methods=['GET', 'POST'])
def render_index_page():
    """
    Renders the main page of the emotion detection application.
    Handles form submission and processes emotion detection requests.

    Returns:
        HTML: The index page with results if form was submitted
    """
    if request.method == 'POST':
        try:
            text_to_analyze = request.form.get('text')

            # Error handling for blank input
            if not text_to_analyze or not text_to_analyze.strip():
                return render_template('index.html', result={
                    'error': 'Invalid text! Please try again.'
                })

            result = emotion_predictor(text_to_analyze)
            return render_template('index.html', result=result)
        except Exception as e:
            return render_template('index.html', result={
                'error': f'An error occurred: {str(e)}'
            })

    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    API endpoint for emotion detection.
    Accepts text as a query parameter and returns emotion analysis.

    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions

    Returns:
        dict: JSON response with emotion scores and dominant emotion
    """
    try:
        text_to_analyze = request.args.get('textToAnalyze')

        # Error handling: return status code 400 for invalid input
        if not text_to_analyze or not text_to_analyze.strip():
            return {
                'error': 'Invalid text! Please try again.'
            }, 400

        response = emotion_predictor(text_to_analyze)

        # Return status code 400 if error in response
        if 'error' in response:
            return response, 400

        return response, 200

    except Exception as e:
        return {
            'error': f'An error occurred: {str(e)}'
        }, 500


@app.errorhandler(404)
def not_found(_error):
    """
    Handles 404 errors.

    Args:
        _error: The error object (unused but required by Flask)

    Returns:
        tuple: Error message and status code
    """
    return {'error': 'Page not found'}, 404


@app.errorhandler(500)
def internal_error(_error):
    """
    Handles 500 internal server errors.

    Args:
        _error: The error object (unused but required by Flask)

    Returns:
        tuple: Error message and status code
    """
    return {'error': 'Internal server error'}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
