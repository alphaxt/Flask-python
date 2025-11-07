#!/bin/bash
# Script to run tests and static code analysis

echo "Running unit tests..."
pytest -v

echo ""
echo "Running Pylint..."
pylint emotion_detection.py app.py test_emotion_detection.py

echo ""
echo "Running Flake8..."
flake8 emotion_detection.py app.py test_emotion_detection.py

echo ""
echo "All checks completed!"

