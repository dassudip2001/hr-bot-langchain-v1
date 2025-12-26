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


class ChatRequest(BaseModel):
    """Chat request model"""
    question: str = Field(..., description="The question to ask the chat agent", min_length=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "What is the HR policy?"
            }
        }


class ChatResponse(BaseModel):
    """Chat response model"""
    answer: str = Field(..., description="The answer from the chat agent")
    status: str = Field(default="success", description="Response status")
    
    class Config:
        json_schema_extra = {
            "example": {
                "answer": "Based on the HR policy...",
                "status": "success"
            }
        }