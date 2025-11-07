# Emotion Detection Application

An AI-based web application that performs emotion detection on customer feedback using IBM Watson Natural Language Understanding (NLP) library.

## Project Overview

This application analyzes text input to detect emotions (anger, disgust, fear, joy, sadness) and identifies the dominant emotion. It's designed for e-commerce companies to analyze customer feedback and improve their products and services.

## Features

- **Emotion Detection**: Analyzes text to detect five core emotions (anger, disgust, fear, joy, sadness)
- **Web Interface**: User-friendly Flask web application with modern UI
- **API Endpoint**: RESTful API for programmatic access
- **Error Handling**: Comprehensive error handling throughout the application
- **Unit Tests**: Complete test suite for all functionality
- **Static Code Analysis**: Configured with Pylint and Flake8

## Project Structure

```
Flask-python/
├── app.py                      # Main Flask application
├── emotion_detection.py        # Emotion detection module using Watson NLP
├── test_emotion_detection.py   # Unit tests
├── setup.py                    # Package configuration
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration
├── .pylintrc                   # Pylint configuration
├── .flake8                     # Flake8 configuration
├── templates/
│   └── index.html              # Web interface template
└── static/
    └── style.css               # CSS styling
```

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd Flask-python
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Watson NLU credentials** (optional for testing):
   - Create a `.env` file in the project root
   - Add your Watson NLU credentials:
     ```
     WATSON_NLU_URL=https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID
     WATSON_NLU_APIKEY=your_api_key_here
     ```
   - Note: If credentials are not provided, the application will use a mock implementation for testing

## Usage

### Running the Web Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   - Open your browser and navigate to `http://localhost:5000`
   - Enter text in the form and click "Detect Emotion"
   - View the emotion analysis results

### Using the API Endpoint

The application provides a REST API endpoint:

```bash
GET /emotionDetector?textToAnalyze=<your_text>
```

Example:
```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy%20today!"
```

Response:
```json
{
  "anger": 0.0,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 0.95,
  "sadness": 0.05,
  "dominant_emotion": "joy"
}
```

## Testing

### Run Unit Tests

```bash
pytest
```

Or with coverage report:
```bash
pytest --cov=emotion_detection --cov=app --cov-report=html
```

### Run Individual Test File

```bash
python -m pytest test_emotion_detection.py -v
```

## Static Code Analysis

### Run Pylint

```bash
pylint emotion_detection.py app.py
```

### Run Flake8

```bash
flake8 emotion_detection.py app.py
```

## Tasks Completed

✅ **Task 1**: Project repository structure created  
✅ **Task 2**: Emotion detection application using Watson NLP library  
✅ **Task 3**: Formatted output of the application  
✅ **Task 4**: Application packaged (setup.py, requirements.txt)  
✅ **Task 5**: Unit tests created and configured  
✅ **Task 6**: Web deployment using Flask  
✅ **Task 7**: Error handling incorporated  
✅ **Task 8**: Static code analysis configured (Pylint, Flake8)  

## Dependencies

- **Flask** (3.0.0): Web framework
- **ibm-watson** (7.0.0): IBM Watson SDK for Natural Language Understanding
- **pytest** (7.4.3): Testing framework
- **pytest-cov** (4.1.0): Coverage plugin for pytest
- **pylint** (3.0.2): Static code analysis
- **flake8** (6.1.0): Linting tool
- **python-dotenv** (1.0.0): Environment variable management

## Error Handling

The application includes comprehensive error handling for:
- Invalid or empty text input
- Missing Watson API credentials (falls back to mock implementation)
- API connection errors
- HTTP errors (404, 500)
- General exceptions

## License

Apache License 2.0

## Author

Created as part of the AI-Based Web Application Development and Deployment final project.
