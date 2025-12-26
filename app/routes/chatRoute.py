from flask import Blueprint
from app.controllers.chatController import ChatController

chatRoute = Blueprint('chat', __name__)

# Initialize controller
chat_controller = ChatController()


@chatRoute.post("/ask")
def ask():
    """Route handler for asking questions to the chat agent"""
    return chat_controller.ask_question()