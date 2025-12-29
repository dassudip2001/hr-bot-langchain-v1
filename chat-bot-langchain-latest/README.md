# Chat Bot with LangChain

A Flask-based RAG (Retrieval-Augmented Generation) chatbot application that answers questions about HR policies using LangChain, OpenAI, and ChromaDB. The application follows a clean architecture pattern with controllers, services, and routes.

## Features

- 🤖 **RAG-based Chatbot**: Uses Retrieval-Augmented Generation to answer questions based on HR policy documents
- 🔍 **Vector Search**: Leverages ChromaDB for semantic search and document retrieval
- 🏗️ **Clean Architecture**: Implements controller-service pattern for maintainable code structure
- 🔐 **Environment-based Configuration**: Secure configuration management using environment variables
- 📊 **Health Check Endpoint**: Monitor application health status
- 🚀 **RESTful API**: Well-structured API endpoints for chat interactions

## Tech Stack

- **Framework**: Flask 3.1.2+
- **LLM**: OpenAI GPT-4.1-mini
- **Vector Database**: ChromaDB
- **Embeddings**: OpenAI text-embedding-3-large
- **Language Chain**: LangChain
- **Validation**: Pydantic
- **Python**: 3.13+

## Project Structure

```
chat-bot-langchain-latest/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── config/
│   │   └── config.py            # Application configuration
│   ├── controllers/
│   │   ├── chatController.py    # Chat request controller
│   │   └── healdthController.py # Health check controller
│   ├── models/
│   │   └── schema.py             # Pydantic models for request/response
│   ├── routes/
│   │   ├── chatRoute.py         # Chat API routes
│   │   └── heldthCheck.py       # Health check routes
│   └── services/
│       └── chatService.py       # Chat business logic & RAG agent
├── chroma_db/                   # ChromaDB persistent storage
├── main.py                      # Application entry point
├── pyproject.toml               # Project dependencies
└── README.md                    # This file
```

## Installation

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip
- OpenAI API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chat-bot-langchain-latest
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -e .
   ```

3. **Create a `.env` file** in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   PORT=5003
   LANGSMITH_API_KEY=your_langsmith_api_key_here  # Optional
   ```

4. **Set up the vector database**
   - The ChromaDB will be automatically initialized on first run
   - Ensure you have trained/ingested documents into the vector store (see `tranning/traning.py`)

## Configuration

The application uses environment variables for configuration. Key settings:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `PORT`: Server port (default: 5003)
- `LANGSMITH_API_KEY`: LangSmith API key for tracing (optional)

Configuration is managed in `app/config/config.py`.

## Running the Application

### Development Mode

```bash
uv run main.py
```

Or with Python directly:
```bash
python main.py
```

The server will start on `http://127.0.0.1:5003` (or the port specified in your `.env` file).

## API Endpoints

### Health Check

**GET** `/api/v1/`

Check the health status of the application.

**Response:**
```json
{
  "message": "OK",
  "status": "healthy",
  "timestamp": "2024-12-26T20:56:49.810000"
}
```

### Ask Question

**POST** `/api/v1/ask`

Ask a question to the HR policy chatbot.

**Request Body:**
```json
{
  "question": "What is the leave policy?"
}
```

**Response:**
```json
{
  "answer": "Based on the HR policy...",
  "status": "success"
}
```

**Error Response (400):**
```json
{
  "error": "Question is required"
}
```

**Error Response (500):**
```json
{
  "error": "An error occurred while processing your request",
  "message": "Error details"
}
```

## Usage Examples

### Using cURL

**Health Check:**
```bash
curl http://127.0.0.1:5003/api/v1/
```

**Ask a Question:**
```bash
curl -X POST http://127.0.0.1:5003/api/v1/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the HR policy for remote work?"}'
```

### Using Python Requests

```python
import requests

# Health check
response = requests.get("http://127.0.0.1:5003/api/v1/")
print(response.json())

# Ask a question
response = requests.post(
    "http://127.0.0.1:5003/api/v1/ask",
    json={"question": "What is the leave policy?"}
)
print(response.json())
```

## Sample Questions

The chatbot can answer a wide range of HR policy questions. Here are some example questions organized by category:

### General HR Policy Questions

- What is the primary objective of having an HR policy in an organization?
- How does the IIA HR policy help in preventing legal issues?
- What are the benefits of maintaining written HR policies and procedures?

### 📌 Recruitment & Selection

- What is the first stage of recruitment for executive positions in IIA?
- Who is the appointing authority for Executive Directors at IIA?
- What documents must a candidate submit before receiving an appointment letter?
- How long is the probation period for new employees in IIA?
- What are the consequences of falsifying educational or professional documents?

### 📌 Training & Development

- What is the purpose of the IIA Excellence Center for Training?
- What is the duration and structure of the induction training for new employees?

### 📌 Dress Code & Uniform

- How often are employees provided with uniforms and formal shoes?
- Under what conditions can female employees choose alternative attire?

### 📌 Performance Appraisal

- What formats are used for performance evaluation on a daily, weekly, and monthly basis?
- List two objectives of the IIA performance appraisal system.

### 📌 Remuneration & Benefits

- How often does IIA review pay scales?
- What benefits does IIA provide to employees besides the basic salary?
- Which social security schemes are employees registered under as per policy?

### 📌 Leave & Transfer

- What is the procedure for applying for leave in IIA?
- How does the transfer policy ensure smooth functioning across chapters?

### 📌 Discipline, Culture & Conduct

- What actions may be taken against employees involved in misconduct?
- How does IIA maintain a culture of high performance and discipline?

### 📌 Gender Policy & Safety

- What protections does the IIA gender policy provide at the workplace?
- Why is safety and health policy crucial for employee productivity?

## Architecture

The application follows a **Controller-Service-Route** pattern:

1. **Routes** (`app/routes/`): Define API endpoints and HTTP methods
2. **Controllers** (`app/controllers/`): Handle HTTP request/response logic, validation, and error handling
3. **Services** (`app/services/`): Contain business logic and interact with external services (LLM, vector DB)
4. **Models** (`app/models/`): Define data schemas using Pydantic

This separation ensures:
- Clean code organization
- Easy testing and maintenance
- Reusable components
- Clear separation of concerns

## RAG Implementation

The chatbot uses a RAG (Retrieval-Augmented Generation) approach:

1. **Document Embedding**: Documents are embedded using OpenAI's `text-embedding-3-large` model
2. **Vector Storage**: Embeddings are stored in ChromaDB for efficient similarity search
3. **Retrieval**: When a question is asked, the system retrieves the top 3 most relevant document chunks
4. **Generation**: The retrieved context is passed to GPT-4.1-mini along with the question to generate an accurate answer

## Development

### Project Dependencies

Dependencies are managed in `pyproject.toml`. Key packages:

- `flask`: Web framework
- `langchain[openai]`: LLM orchestration
- `langchain-chroma`: ChromaDB integration
- `chromadb`: Vector database
- `pydantic`: Data validation
- `python-dotenv`: Environment variable management

### Adding New Features

1. **New Route**: Add route in `app/routes/`
2. **New Controller**: Create controller in `app/controllers/`
3. **New Service**: Add business logic in `app/services/`
4. **New Model**: Define schema in `app/models/schema.py`

## Troubleshooting

### Common Issues

1. **OpenAI API Key Error**: Ensure `OPENAI_API_KEY` is set in your `.env` file
2. **ChromaDB Connection Error**: Check if `chroma_db` directory has proper permissions
3. **Port Already in Use**: Change the `PORT` in your `.env` file

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on the repository.

