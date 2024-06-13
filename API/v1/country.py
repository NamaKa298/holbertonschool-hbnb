from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager as Countries_repository

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello World"}), 200

@app.route('/countries', methods=['POST'])
def create_countrie():
    from Model.country import Country
    data = request.get_json()
    Country = Country(**data)
    Countries_repository.save(Country)
    return jsonify(Country.to_dict()), 201

@app.route('/Countries', methods=['GET'])
def read_Countries():
    Countries = Countries_repository.all("Countries")
    return jsonify([Country.to_dict() for Country in Countries]), 200

@app.route('/Countries/<id>', methods=['GET'])
def read_Country(email):
    Country = Countries_repository.find_by_email(email)
    if Country is None:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(Country.to_dict()), 200

@app.route('/Countries/<id>', methods=['PUT'])
def update_Country(email):
    Country = Countries_repository.find_by_email(email)
    if Country is None:
        return jsonify({"error": "Country not found"}), 404
    data = request.get_json()
    Country.update(data)
    Countries_repository.save(Country)
    return jsonify(Country.to_dict()), 200

@app.route('/Countries/<id>', methods=['DELETE'])
def delete_Country(email):
    Country = Countries_repository.find_by_email(email)
    if Country is None:
        return jsonify({"error": "Country not found"}), 404
    Countries_repository.delete(Country)
    return jsonify({}), 204

