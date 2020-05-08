import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import time
from server.utils import generateCityList, generateDictArray
from server.city import City
from server.simulated_annealing import SimulatedAnnealing

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/hello')
@cross_origin()
def hello():
    return 'Hello from Enzo Lizama & Rodrigo Guadalupe!'


@app.route('/calculate_route', methods=['POST'])
@cross_origin()
def calculate_route():
    post_data = request.data.decode("utf-8")
    data = json.loads(post_data)
    cities = data["markers"]

    temperature = None if not float(
        data["temperature"]) else float(data["temperature"])
    coldIndex = None if not float(
        data["coldIndex"]) else float(data["coldIndex"])
    nIterations = None if not int(
        data["iteractions"]) else float(data["iteractions"])

    cities = [c for c in cities]

    start = time.time()
    cityList = generateCityList(cities)
    sa = SimulatedAnnealing(cityList, temperature=temperature,
                            coldIndex=coldIndex, stoppingIteration=nIterations)
    route, distance = sa.executeAlgorithm()

    route = generateDictArray(route, cityList)
    end = time.time()

    return {"time": round(end-start, 2), "route": route, "distance": round(distance, 2)}


if __name__ == "__main__":
    app.run(host='localhost')
