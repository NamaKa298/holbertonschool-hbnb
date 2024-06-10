from flask import Flask, request, jsonify
from Model.user import User
from Persistence.database import Database
from Persistence.datamanager import DataManager

app = Flask(__name__)
db = Database()
user_repository = DataManager(db)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    user_repository.save(user)
    return jsonify(user.to_dict()), 201

@app.route('/users', methods=['GET'])
def read_users():
    users = user_repository.all()
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

if __name__ == '__main__':
    app.run()
