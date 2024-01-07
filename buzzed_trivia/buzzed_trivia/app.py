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
def login():
    return login()


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
