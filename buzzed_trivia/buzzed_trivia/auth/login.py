from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash

USER_DATA = {
    "username": "testuser",
    "password_hash": "pbkdf2:sha256:150000$vlIE7EWO$10b..."
}


def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Both username and password are required"}), 400

    user = USER_DATA
    if user and check_password_hash(user['password_hash'], password):
        # The user has been successfully authenticated
        resp = make_response(jsonify({"message": "Logged in successfully"}))
        resp.set_cookie("session_id", "Your-Unique-Session-Id", httponly=True, samesite='Lax', secure=True)
        return resp
    else:
        return jsonify({"message": "Invalid username or password"}), 401
