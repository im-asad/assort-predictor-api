from flask import Flask, request, jsonify
import flask
from PIL import Image
import os
from keras.applications import VGG16
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from keras.models import Sequential
from keras.models import load_model
import numpy as np
import io
import pickle

app = Flask(__name__)

def loadModel():
    # load the trained model's .h5 file
    global model
    model = load_model('my_model_dimensions_84point5.h5')
    return model

def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    # image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image

model = loadModel()

import routes

if __name__ == '__main__':
    app.run(debug = False, threaded = False)