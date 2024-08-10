# EmotionDetector-FinalProject

## Description
EmotionDetector-FinalProject is the final project developed as part of the Coursera course "Developing AI Applications with Python and Flask". This project demonstrates how to create an AI-powered Python application using embeddable Watson AI libraries, including Natural Language Processing (NLP), text-to-speech, and speech-to-text libraries.

These libraries offer a variety of functions, such as sentiment analysis, emotion detection, text classification, and language detection, which are all powered by pretrained AI models available on the Skills Network Labs Cloud IDE. This project covers the entire development lifecycle, from creating and packaging the AI application to testing, deploying, and ensuring code quality.

The course can be found here: [Developing AI Applications with Python and Flask](https://www.coursera.org/learn/python-project-for-ai-application-development/)

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Technologies Used
- **Python**: Programming language used for building the application.
- **Watson NLP Library**: For sentiment analysis, emotion detection, and other NLP tasks.
- **Watson Text-to-Speech Library**: Converts written text into natural-sounding audio.
- **Watson Speech-to-Text Library**: Transcribes spoken audio into written text.
- **Flask**: Framework used for deploying the application as a web service.
- **PEP8**: Python style guide followed for code quality and consistency.

## Installation
To set up this project locally, follow these steps:

1. **Clone the Repository:**
   git clone https://github.com/your-username/EmotionDetector-FinalProject.git
   cd EmotionDetector-FinalProject

2. **Install Dependencies:**
    
    Install the necessary Python libraries:

        pip install -r requirements.txt

3. **Run the Application:**

    Start the Flask web server:

        flask run

## Usage ##

Once the application is running, you can interact with it via the web interface or by sending API requests to perform sentiment analysis, emotion detection, and other NLP tasks using the Watson NLP libraries.

## Features ##
- Sentiment Analysis: Analyzes text to determine the sentiment (positive, negative, neutral).
- Emotion Detection: Identifies emotions conveyed in text (e.g., joy, anger, sadness).
- Text-to-Speech: Converts written text into spoken audio.
- Speech-to-Text: Transcribes spoken audio into written text.
- Error Handling: Responds appropriately to errors, with support for HTTP 500 status code.
- Unit Testing: Comprehensive tests to validate the application's functionality.
- Static Code Analysis: Ensures code adheres to PEP8 guidelines.

## License ##
This project is licensed under the MIT License. See the LICENSE file for more information.

