import csv
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def data():
    with open("data.csv", mode='r') as f:
        return jsonify(list(csv.DictReader(f)))

if __name__ == "__main__":
    app.run(debug=True)
