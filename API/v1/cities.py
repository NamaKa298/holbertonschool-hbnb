from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager as City_repository

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello World"}), 200

@app.route('/Cities', methods=['POST'])
def create_City():
    from Model.city import City
    data = request.get_json()
    City = City(**data)
    City_repository.save(City)
    return jsonify(City.to_dict()), 201

@app.route('/Cities', methods=['GET'])
def read_Cities():
    Cities = City_repository.all("Cities")
    return jsonify([City.to_dict() for City in Cities]), 200

@app.route('/Cities/<id>', methods=['GET'])
def read_City(email):
    City = City_repository.find_by_email(email)
    if City is None:
        return jsonify({"error": "City not found"}), 404
    return jsonify(City.to_dict()), 200

@app.route('/Cities/<id>', methods=['PUT'])
def update_City(email):
    City = City_repository.find_by_email(email)
    if City is None:
        return jsonify({"error": "City not found"}), 404
    data = request.get_json()
    City.update(data)
    City_repository.save(City)
    return jsonify(City.to_dict()), 200

@app.route('/Cities/<id>', methods=['DELETE'])
def delete_City(email):
    City = City_repository.find_by_email(email)
    if City is None:
        return jsonify({"error": "City not found"}), 404
    City_repository.delete(City)
    return jsonify({}), 204

