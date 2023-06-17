from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/deploy')
def deploy():
    return "Deploy works!"


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
