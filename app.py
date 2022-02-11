from flask import Flask, jsonify, request
from class125 import get_predictions

app=Flask(__name__)
@app.route("/predict-digit-data",methods=["POST"])

def predict_data():
    image=request.file.get("digit")
    predict=get_predictions(image)
    return jsonify({
       "prediction":predict
    }),200

if(__name__== "__main__"):
    app.run(debug=True)

