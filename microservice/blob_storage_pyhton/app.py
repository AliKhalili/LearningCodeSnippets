import time

from flask import Flask, g, request, jsonify

from api.blob import blob_bp
from api.health import health_bp
from helpers.configuration import Configuration


def register_extensions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(blob_bp)
    app.register_blueprint(health_bp)


def register_error_handlers(app):
    pass


def create_app(config=Configuration):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    @app.before_request
    def before_request():
        g.request_start_time = time.time()
        g.request_time = lambda: f'{time.time() - g.request_start_time:.5f}s'

    print(app.url_map)
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
