from flask import Flask, request, jsonify
import flask
from PIL import Image
import io
from __main__ import app, prepare_image, model

labelMap = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic']

@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(192, 144))
            # classify the input image and then initialize the list of predictions to return to the client
            preds = model.predict(image)
            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    outputArr = list(preds[0])
    index = outputArr.index(max(outputArr))
    return jsonify({'label': labelMap[index]})

@app.route('/', methods=['GET'])
def get():
    return jsonify({'message': 'App is running.'})