from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def fac_app():
        return 'OK'

    return fac_app
