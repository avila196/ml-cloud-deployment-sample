from flask import Flask, request
from flasgger import Swagger
from datetime import date
import glob
import os

import json

app = Flask("Topics Classifier!")
swagger = Swagger(app)

#Class that defines a Predictor object to make all predictions
class Predictor:
    def __init__(self, topics_path="topics.json"):
        """ 
        Constructor/initializer of the predictor.
        """
        
        #Set dictionary mapping labels
        with open(topics_path, "r") as f:
            self.classes = json.load(f)

    def predict(self, text):
        """
        Makes a prediction of the topic given the input text and returns the topic for it
        For this dummy server, a dummy prediction is made
        """
        #To predict, we use the key as (length text) mod (total topics)
        predicted_class = len(text) % len(self.classes)
        return self.classes[str(predicted_class)]

#Initialize object to make all predictions
predictor = Predictor()

@app.route("/health", methods=["GET"])
def healthcheck():
    return "All good!"

@app.route("/predict_files_local", methods=["POST"])
def predict():
    """ Endpoint to predict the topic for a given text
    ---
    parameters:
        - name: location
          in: formData
          type: string
          required: true
          description: Location for text files to classify
    responses:
        200:
            description: Topics found for files
    """
    try:
        location = request.form["location"]
        #For testing purposes, the location is just a folder within the container with 3 files
        #Loop through files and find the topic for each
        all_topics = []
        for file in glob.glob(os.path.join(location, "*.txt")):
            #Read file's content and predict its topic
            with open(file, "r") as f:
                content = f.read()
                all_topics.append(file + ": " + predictor.predict(content))

        #For testing, we're just logging all topics into the console. So we return a message for them
        dt = date.today()
        timestamp = dt.strftime("%d/%m/%Y")
        return f"Predictions made by {timestamp}: {str(all_topics)}."
    except Exception as e:
        return "Error making predictions: " + str(e)
    
#TODO 1: Add /predict endpoint for batch files located in S3 or GS

#TODO 2: Add /predict endpoint for direct prediction (input text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)