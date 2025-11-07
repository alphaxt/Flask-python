from setuptools import setup, find_packages

setup(
    name="emotion-detection",
    version="1.0.0",
    description="AI-based emotion detection web application using Watson NLP",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "flask==3.0.0",
        "ibm-watson==7.0.0",
        "python-dotenv==1.0.0",
    ],
    python_requires=">=3.8",
)

