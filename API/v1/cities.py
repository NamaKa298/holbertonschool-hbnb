from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager as city_repository

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello World"}), 200

@app.route('/cities', methods=['POST'])
def create_user():
    from Model.city import City
    data = request.get_json()
    city = City(**data)
    city_repository.save(city)
    return jsonify(city.to_dict()), 201

@app.route('/cities', methods=['GET'])
def read_users():
    cities = city_repository.all("City")
    return jsonify([cities[id].to_dict() for id in cities]), 200

@app.route('/cities/<id>', methods=['GET'])
def read_user(id):
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    return jsonify(city.to_dict()), 200

@app.route('/cities/<id>', methods=['PUT'])
def update_user(id):
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    data = request.get_json()
    city_repository.update(city, **data)
    return jsonify(city.to_dict()), 200

@app.route('/cities/<id>', methods=['DELETE'])
def delete_user(id):
    city = city_repository.get(id, "City")
    if city is None:
        return jsonify({"error": "City not found"}), 404
    city_repository.delete(city, "City")
    return jsonify({}), 204