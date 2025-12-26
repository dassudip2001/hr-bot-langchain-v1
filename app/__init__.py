from flask import Flask
def create_app():

    app = Flask(__name__)

    """Helth Registering Blueprints  """
    from app.routes.heldthCheck import health
    app.register_blueprint(health,url_prefix="/api/v1")

    return app