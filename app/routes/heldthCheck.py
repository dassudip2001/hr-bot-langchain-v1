import datetime
from flask import Blueprint, jsonify

from app.models.schema import HealthResponse
heldth= Blueprint('heldth', __name__)

health = Blueprint("health", __name__)

@health.route("/", methods=["GET"])
def health_check(): # type: ignore
    health_response = HealthResponse(
        message="OK",
        status="healthy",
        timestamp=datetime.datetime.now().isoformat()
    )
    return jsonify(health_response.model_dump()), 200