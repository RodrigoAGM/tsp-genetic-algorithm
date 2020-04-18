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
    return 'Hello from Enzo Lizama & Rodrigo Guadalupe!'


@app.route('/calculate_route', methods=['POST'])
@cross_origin()
def calculate_route():
    post_data = request.data.decode("utf-8")
    data = json.loads(post_data)
    cities = data["cities"]
    generations_number = int(data["generationNumber"])
    mutation_probability = float(data["mutationProbability"])
    initial_poblation = int(data["initialPoblation"])
    elite_size = int(data["eliteSize"])
    cities = [c for c in cities]

    start = time.time()
    cityList = generateCityList(cities)
    route, distance = geneticAlgorithm(cityList=cityList,
                                       nGenerations=generations_number,
                                       mutationProb=mutation_probability / 100,
                                       initialPopulation=initial_poblation,
                                       eliteSize=elite_size)
    route = generateDictArray(route)
    end = time.time()
    return {"time": round(end-start, 2), "route": route, "distance": round(distance, 2)}


if __name__ == "__main__":
    app.run(host='localhost')
