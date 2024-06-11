from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    return jsonify(data), 201

@app.route('/user', methods=['GET'])
def get_users():
    return jsonify({"users": []}), 200

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({"user_id": user_id}), 200

@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    return jsonify({"user_id": user_id, **data})

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({}), 204

if __name__ == "__main__":
    app.run()
