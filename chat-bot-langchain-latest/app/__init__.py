from flask import Flask

def create_app():

    app = Flask(__name__)

    """Helth Registering Blueprints  """
    from app.routes.heldthCheck import heldth
    app.register_blueprint(heldth,url_prefix="/api/v1")

    """Chat Registering Blueprints """
    from app.routes.chatRoute import chatRoute
    app.register_blueprint(chatRoute,url_prefix="/api/v1")

    return app