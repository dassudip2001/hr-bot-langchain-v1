# Chat Application - HR Policy Q&A Assistant

A full-stack chat application featuring a RAG (Retrieval-Augmented Generation) powered chatbot that answers questions about HR policies. The application consists of a Flask backend API and a Next.js frontend client.

## 🚀 Features

- 🤖 **RAG-based Chatbot**: Uses Retrieval-Augmented Generation to answer questions based on HR policy documents
- 🔍 **Vector Search**: Leverages ChromaDB for semantic search and document retrieval
- 🎨 **Modern Frontend**: Next.js 16 with React 19, TypeScript, and Tailwind CSS
- 🏗️ **Clean Architecture**: Implements controller-service pattern for maintainable code structure
- 🔐 **Environment-based Configuration**: Secure configuration management using environment variables
- 📊 **Health Check Endpoint**: Monitor application health status
- 🚀 **RESTful API**: Well-structured API endpoints for chat interactions

## 📁 Project Structure

```
chat-application/
├── chat-bot-langchain-latest/    # Backend Flask API
│   ├── app/
│   │   ├── config/                # Application configuration
│   │   ├── controllers/           # Request controllers
│   │   ├── models/                # Pydantic models
│   │   ├── routes/                # API routes
│   │   └── services/              # Business logic & RAG agent
│   ├── chroma_db/                 # ChromaDB persistent storage
│   ├── main.py                    # Application entry point
│   ├── pyproject.toml             # Python dependencies
│   └── docker-compose.yml         # Docker configuration
│
└── chat-client/                   # Frontend Next.js client
    ├── app/                      # Next.js app directory
    ├── public/                  # Static assets
    ├── package.json             # Node.js dependencies
    └── tsconfig.json            # TypeScript configuration
```

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask 3.1.2+
- **LLM**: OpenAI GPT-4.1-mini
- **Vector Database**: ChromaDB
- **Embeddings**: OpenAI text-embedding-3-large
- **Language Chain**: LangChain
- **Validation**: Pydantic
- **Python**: 3.13+

### Frontend
- **Framework**: Next.js 16.1.1
- **UI Library**: React 19.2.3
- **Language**: TypeScript 5+
- **Styling**: Tailwind CSS 4
- **Package Manager**: Bun

## 📋 Prerequisites

- Python 3.13 or higher
- Node.js 20+ (or Bun)
- OpenAI API Key
- Git

## 🔧 Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd chat-bot-langchain-latest
```

2. Install dependencies using `uv` (recommended) or `pip`:
```bash
# Using uv
uv pip install -e .

# Or using pip
pip install -e .
```

3. Create a `.env` file in the backend directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
PORT=5000
FLASK_ENV=development
```

4. (Optional) Set up ChromaDB using Docker:
```bash
docker-compose -f chroma-docker-compose.yml up -d
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd chat-client
```

2. Install dependencies:
```bash
# Using bun (recommended)
bun install

# Or using npm
npm install
```

## 🚀 Running the Application

### Start Backend Server

```bash
cd chat-bot-langchain-latest
python main.py
```

The backend API will be available at `http://localhost:5000`

### Start Frontend Client

```bash
cd chat-client
bun dev
# or
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 📡 API Endpoints

### Chat Endpoint
```http
POST /api/v1/ask
Content-Type: application/json

{
  "question": "What is the leave policy for employees?"
}
```

**Response:**
```json
{
  "answer": "Based on the HR policy document...",
  "status": "success"
}
```

### Health Check
```http
GET /api/v1/health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "Service is running"
}
```

## 🔄 How RAG Works

1. **Document Processing**: HR policy PDFs are split into chunks and converted to vector embeddings
2. **Vector Storage**: Embeddings stored in ChromaDB for fast similarity search
3. **Query Processing**: User questions are converted to embeddings
4. **Retrieval**: System finds the top 3 most relevant document chunks
5. **Generation**: GPT-4.1-mini generates answer using retrieved context

## 🐳 Docker Support

### Backend with Docker

```bash
cd chat-bot-langchain-latest
docker-compose up -d
```

### ChromaDB with Docker

```bash
cd chat-bot-langchain-latest
docker-compose -f chroma-docker-compose.yml up -d
```

## 🧪 Testing

### Backend Testing
```bash
cd chat-bot-langchain-latest
python testing/testing.py
```

## 📝 Environment Variables

### Backend (.env)
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `PORT`: Server port (default: 5000)
- `FLASK_ENV`: Environment mode (development/production)

### Frontend
Configure API endpoint in your frontend code to point to the backend URL.

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**: Ensure `OPENAI_API_KEY` is set in your `.env` file
2. **ChromaDB Connection Error**: Check if `chroma_db` directory has proper permissions
3. **Port Already in Use**: Change the `PORT` in your `.env` file
4. **Module Not Found**: Ensure all dependencies are installed using `uv pip install -e .` or `pip install -e .`

## 📚 Development

### Adding New Features

**Backend:**
1. **New Route**: Add route in `app/routes/`
2. **New Controller**: Create controller in `app/controllers/`
3. **New Service**: Add business logic in `app/services/`
4. **New Model**: Define schema in `app/models/schema.py`

**Frontend:**
1. Add new pages in `app/` directory
2. Create components as needed
3. Update API calls to match backend endpoints

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions, please open an issue on the repository.

## 👤 Author

**Sudip Das**
- GitHub: [@dassudip2001](https://github.com/dassudip2001)

---

**Note**: This project was created as part of the IBM SkillsBuild Winter Certification Program – Applied Artificial Intelligence.

