import datetime
from flask import Blueprint, jsonify

from app.controllers.healdthController import HealdthController
from app.models.schema import HealthResponse
heldth= Blueprint('heldth', __name__)


@heldth.route("/", methods=["GET"])
def health_check(): # type: ignore
    return HealdthController.health_check()