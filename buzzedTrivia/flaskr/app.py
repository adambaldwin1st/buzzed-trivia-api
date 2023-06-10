from flask import Flask


def create_app(environ, start_response):
    # create and configure the app
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello"

    return app
