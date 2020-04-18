import os

from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from server.city import City
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/hello')
@cross_origin()
def hello():
    return 'Hello, World!'


@app.route('/calculate_route', methods=['POST'])
@cross_origin()
def calculate_route():
    post_data = request.data.decode("utf-8")
    cities = json.loads(post_data)
    cities = [c for c in cities]
    # TODO: calculate routes and await for response
    print(cities)
    return {"time": 1213.12, "cities": cities, "distance": 121}


if __name__ == "__main__":
    app.run(host='localhost')
