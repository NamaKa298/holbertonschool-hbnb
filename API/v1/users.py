from flask import request, jsonify
from API.v1.app import app
from Model.user import User
from Persistence.datamanager import data_manager as user_repository

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello World"}), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    user_repository.save(user)
    return jsonify(user.to_dict()), 201

@app.route('/users', methods=['GET'])
def read_users():
    users = user_repository.all("users")
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/<id>', methods=['GET'])
def read_user(email):
    user = user_repository.find_by_email(email)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@app.route('/users/<id>', methods=['PUT'])
def update_user(email):
    user = user_repository.find_by_email(email)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user.update(data)
    user_repository.save(user)
    return jsonify(user.to_dict()), 200

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(email):
    user = user_repository.find_by_email(email)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user_repository.delete(user)
    return jsonify({}), 204

