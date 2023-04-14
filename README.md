# Imagine-Coders_COC
Project Title: Fake Profile Detection using Customized Face Detection Model

## Overview:
This project is aimed at developing an API that can detect fake profiles by identifying if the profile picture is an actual face or a cartoon/distorted image. Additionally, the API will also be able to detect the gender of the person in the image. The project will be built upon a customized face detection model using open source tools and existing models to ensure accuracy and efficiency. The API will have a simple interface and a minimal response time, making it easy to use and implement in various applications.

## Features:

Detects faces and gives out probabilities of having a face in an array.
Detects only actual faces. Cartoon or distorted images shouldn't be detected.
Detects gender from the image.
Uses a customized face detection model to ensure accuracy and efficiency.
Uses open source tools and existing models.
Has a simple interface.
Minimal response time.
## Technologies:

Python
Flask framework
OpenCV
TensorFlow

## Usage:
Send a POST request with an image URL in the request data.
The API will return an array of probabilities indicating the presence of a face in the image, a binary classification indicating if the image contains an actual face, and the gender of the person in the image.
## Contributing:
Contributions are welcome. You can open an issue for any bugs or feature requests, and create a pull request to suggest improvements.
