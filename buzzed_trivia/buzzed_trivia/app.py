from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
from auth.login import login
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:the_hive_password/44.201.142.120:5432/the_hive'
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)

from models import GameSession

@app.route('/')
def index():
    return 'Buzzed Trivia API'


@app.route('/login', methods=['POST'])
def login_endpoint():
    return login()


# In memory database for game sessions
game_sessions = {}


@app.route('/api/create-session', methods=['POST'])
def create_session():
    session_data = request.json
    room_code = ''.join(random.choices(string.ascii_uppercase, k=4))

    # Add additional validation to ensure the room_code is unique
    while room_code in game_sessions:
        room_code = ''.join(random.choices(string.ascii_uppercase, k=4))

    game_sessions[room_code] = session_data
    return jsonify({'room_code': room_code}), 201


@app.route('/api/join-session/<room_code>', methods=['GET'])
def join_session(room_code):
    session = game_sessions.get(room_code)
    if session is None:
        return jsonify({'error': 'Invalid room code'}), 400

    return jsonify(session), 200


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
