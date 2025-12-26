from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    """Health check response model"""
    message: str = Field(..., description="Health status message")
    status: str = Field(..., description="Health status")
    timestamp: str = Field(..., description="Current timestamp in ISO format")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "OK",
                "status": "healthy",
                "timestamp": "2024-01-01T12:00:00.000000"
            }
        }