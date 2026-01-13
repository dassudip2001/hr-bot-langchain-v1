from flask import Flask
from flask_cors import CORS
import os

def create_app():

    app = Flask(__name__)

    # Configure CORS properly to handle credentials
    # Get allowed origins from environment or default to common dev ports
    allowed_origins = os.getenv(
        "CORS_ORIGINS", 
        "http://localhost:3000,http://localhost:3001,http://127.0.0.1:3000"
    ).split(",")
    
    CORS(
        app,
        origins=allowed_origins,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        supports_credentials=True
    )

    """Helth Registering Blueprints  """
    from app.routes.heldthCheck import heldth
    app.register_blueprint(heldth,url_prefix="/api/v1")

    """Chat Registering Blueprints """
    from app.routes.chatRoute import chatRoute
    app.register_blueprint(chatRoute,url_prefix="/api/v1")

    return app