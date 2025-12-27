import datetime

from flask import jsonify
from app.models.schema import HealthResponse


class HealdthController:
    """Controller for handling health check requests"""
    @staticmethod
    def health_check(): 
        health_response = HealthResponse(
            message="OK",
            status="healthy",
            timestamp=datetime.datetime.now().isoformat()
        )
        return jsonify(health_response.model_dump()), 200