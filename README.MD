# Animal Face Classification

This is a simple project to practice machine learning techniques and the workflow to deploy an application which applies the created model.

## Structure

The project is compound of two parts:

* api: a simple RESTful API which receive requests to predict which kind of animal was supplied
* webapp: a simple application running over the web browser, it receives an image and request the API to make the prediction

## Technologies

* Python 3.8
* Tensorflow
* Sklearn
* Streamlit
* FastAPI

## About the predictive model

The model creation is documented in a Jupyter notebook found at `api/models`.
The core of this model is the [deepfeatx](https://github.com/wittmannf/deepfeatx) library, which uses a pre-trained convolutional neural network to convert images into feature vectors.


## Running locally

You can run this project locally using either Docker or local Python installation.

The default configuration will start the webapp at `http://localhost:4200` and the api at `http://localhost:8000`.

### Docker

Simply run `docker-compose up` at the root of the project. It will build images and run containers.

### Local Python installation

Both api and webapp have a list of required dependencies, then you need to install them before running.

To do so, run `pip install -r requirements.txt` inside each folder.


## Live demo

You can access the webapp [here](http://animal-face-classification.herokuapp.com/).

> **NOTE**: you may experience some error at first try due to deployment environment. The api service will be started when you submit the first prediction, so this startup process can take a while.