import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import time
from server.genetic_algorithm import geneticAlgorithm
from server.utils import generateCityList, generateDictArray
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

    start = time.time()
    cityList = generateCityList(cities)
    route, distance = geneticAlgorithm(cityList, 500, 0.05, 100, 20)
    route = generateDictArray(route)
    end = time.time()
    # TODO: calculate routes and await for response
    print(route)
    return {"time": round(end-start,2), "route": route, "distance": round(distance,2)}


if __name__ == "__main__":
    app.run(host='localhost')
