from flask import request, jsonify
from API.v1.app import app
from Persistence.datamanager import data_manager as country_repository

@app.route('/countries', methods=['GET'])
def read_countries():
    countries = country_repository.all("Country")
    return jsonify([countries[id].to_dict() for id in countries]), 200

@app.route('/countries/<id>', methods=['GET'])
def read_country(id):
    country = country_repository.get(id, "Country")
    if country is None:
        return jsonify({"error": "Country not found"}), 404
    return jsonify(country.to_dict()), 200

@app.route('/countries/<id>/cities', methods=['GET'])
def read_country_cities(id):
    country = country_repository.get(id, "Country")
    if country is None:
        return jsonify({"error": "Country not found"}), 404
    cities = country.cities
    return jsonify([city.to_dict() for city in cities]), 200
