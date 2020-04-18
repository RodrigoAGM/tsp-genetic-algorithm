# import os

# from flask import Flask, request
# import json
# from server.city import City
# app = Flask(__name__)


# @app.route('/hello')
# def hello():
#     return 'Hello, World!'


# @app.route('/calculate_route', methods=['POST'])
# def calculate_route():
#     post_data = request.data.decode("utf-8")
#     cities = json.dumps(post_data)
#     cities = [City(c['id'], c['x'], c['y']) for p in cities]
#     print(cities)
#     return {"time": 1213.12, "cities": cities, "distance": 121}


# if __name__ == "__main__":
#     app.run(host='0.0.0.0')
