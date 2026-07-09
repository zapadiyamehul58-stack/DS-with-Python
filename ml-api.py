from flask import Flask, jsonify
from sklearn.tree import DecisionTreeClassifier
import numpy as np

app = Flask(__name__)

X = np.array([[2], [4], [6]])
y = np.array(['birds', 'dog', 'spider'])

model = DecisionTreeClassifier()
model.fit(X, y)

@app.route('/')
def home():
    return """
    <h2>Animal prediction</h2>
    <p>Click the link below to predict an animal</p>
    <a href="/predict">predict animal</a>
    """

@app.route("/predict")
def predict():
    legs = 2
    animal = model.predict([[legs]])
    return jsonify({
        "Number of legs": legs,
        "predicted animal": animal[0]
    })

if __name__ == "__main__":
    app.run(port=5001,debug=True)
