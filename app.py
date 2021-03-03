from joblib import load
import json
import numpy as np
from flask import Flask, jsonify, render_template, url_for, request
import pickle
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
#################################################
# HTML ROUTES
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/enrollment")
def treatment():
    return render_template("matt.html")
@app.route("/predictor")
def test():
    return render_template("predictor.html")
@app.route("/results", methods=["POST", "GET"])
def results():
    print("hello")
    if request.method=="POST":
    # read data, do for each question, make sure the features are in correct order
        gre = int(request.form['gre'])
        print('gre')
        toefl = int(request.form['toefl'])
        rating = int(request.form['rating'])
        gpa = float(request.form['gpa'])
        research = int(request.form['research'])
    
        # user input list
        features = [gre, toefl , rating, gpa, research]
        final_features = [np.array(features)]
        final_shape = np.reshape(final_features,(1,-1))
        # load model
        # model = load('model.sav')
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)

        prediction = model.predict(final_shape)
        print(prediction)

        if prediction >= .5:
            return render_template("yes.html")
        else:
            return render_template("no.html")
        return render_template('predictor.html')
    else: 
        print("this gotta work")
        return render_template("predictor.html")
@app.route("/analytics")
def analytics():
    return render_template("analytics.html")
if __name__ == '__main__':
    app.run(debug=True)