from flask import request, jsonify
from app.services.chatService import ask_agent


class ChatController:
    """Controller for handling chat-related requests"""
    
    @staticmethod
    def ask_question():
        """
        Handle POST request to ask a question to the chat agent
        
        Returns:
            JSON response with answer or error message
        """
        try:
            data = request.get_json()
            
            if not data:
                return jsonify({"error": "Request body is required"}), 400
            
            question = data.get("question", "")
            
            if not question:
                return jsonify({"error": "Question is required"}), 400
            
            # Call service to get answer
            answer = ask_agent(question)
            
            return jsonify({
                "answer": answer,
                "status": "success"
            }), 200
            
        except Exception as e:
            return jsonify({
                "error": "An error occurred while processing your request",
                "message": str(e)
            }), 500

