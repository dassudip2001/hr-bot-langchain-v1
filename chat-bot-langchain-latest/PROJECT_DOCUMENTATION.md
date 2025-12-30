# AI Agent Creation Project - HR Q&A Assistant
## IBM SkillsBuild Winter Certification Program – Applied Artificial Intelligence

---

## Project Title
**HR Policy Q&A Assistant - An AI-Powered Chatbot for Automated Employee Support**

---

## Student Details
- **Name**: Sudip Das
- **College**: Vidyasagar University
- **Project Type**: Chatbot / Q&A Assistant
- **Submission Date**: December 2025

---

## 1. Problem Statement & Use Case

### Problem Statement
HR departments in organizations frequently receive repetitive questions from employees about company policies, leave policies, remote work guidelines, benefits, and other HR-related matters. Answering these questions manually:
- Consumes significant HR staff time
- Leads to inconsistent responses
- Creates delays in employee support
- Reduces HR productivity for strategic tasks

### Use Case
**HR Policy Q&A Assistant** - An intelligent chatbot that:
- Automatically answers employee questions about HR policies
- Provides instant, consistent, and accurate responses 24/7
- Reduces HR workload by handling repetitive queries
- Uses company's actual HR policy documents as knowledge base
- Enables HR staff to focus on complex, strategic tasks

### Business Value
- **Time Savings**: Reduces HR response time from hours to seconds
- **Consistency**: Ensures all employees receive accurate, policy-based answers
- **Scalability**: Handles unlimited queries simultaneously
- **Cost Efficiency**: Reduces need for additional HR support staff
- **Employee Satisfaction**: Provides instant answers, improving employee experience

---

## 2. AI Approach and Tools Used

### AI Approach: Retrieval-Augmented Generation (RAG)

The project uses **RAG (Retrieval-Augmented Generation)**, a state-of-the-art AI technique that combines:
1. **Information Retrieval**: Semantic search through company documents
2. **Language Generation**: AI-powered natural language responses

### How It Works

```
User Question → Vector Search → Retrieve Relevant Context → Generate Answer
```

1. **Document Processing**: HR policy PDFs are split into chunks and converted to vector embeddings
2. **Vector Storage**: Embeddings stored in ChromaDB for fast similarity search
3. **Query Processing**: User questions are converted to embeddings
4. **Retrieval**: System finds the 3 most relevant document chunks
5. **Generation**: AI model (GPT-4.1-mini) generates answer using retrieved context

### AI Concepts Applied

- **Natural Language Processing (NLP)**: Understanding and processing human questions
- **Vector Embeddings**: Converting text to numerical representations for semantic search
- **Semantic Search**: Finding relevant information based on meaning, not just keywords
- **Large Language Models (LLMs)**: GPT-4.1-mini for generating human-like responses
- **RAG Architecture**: Combining retrieval and generation for accurate, context-aware answers

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | OpenAI GPT-4.1-mini | Generate natural language responses |
| **Embeddings** | OpenAI text-embedding-3-large | Convert text to vectors |
| **Vector Database** | ChromaDB | Store and search document embeddings |
| **Framework** | LangChain | Orchestrate AI workflows |
| **Web Framework** | Flask | RESTful API for interactions |
| **Language** | Python 3.13+ | Core programming language |

### Libraries Used

- `langchain[openai]`: AI orchestration and agent creation
- `langchain-chroma`: ChromaDB integration
- `chromadb`: Vector database
- `openai`: LLM and embeddings API
- `flask`: Web API framework
- `pydantic`: Data validation
- `pypdf`: PDF document processing

---

## 3. Project Architecture

### System Design

```
┌─────────────┐
│   User      │
│  (Employee) │
└──────┬──────┘
       │ HTTP POST
       │ {question: "..."}
       ▼
┌─────────────────┐
│  Flask API      │
│  /api/v1/ask    │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│ Chat Controller │
│  (Validation)   │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Chat Service   │
│  (AI Agent)     │
└──────┬──────────┘
       │
       ├──► Vector Search (ChromaDB)
       │    └─► Retrieve top 3 chunks
       │
       └──► LLM (GPT-4.1-mini)
            └─► Generate answer
```


---

## 4. Functionality Demonstration

### Input → Processing → Output Flow

#### Example 1: Leave Policy Question

**Input:**
```json
POST /api/v1/ask
{
  "question": "What is the leave policy for employees?"
}
```

**Processing:**
1. Question converted to embedding vector
2. Vector search finds relevant policy sections
3. Top 3 chunks retrieved from ChromaDB
4. GPT-4.1-mini generates answer using context

**Output:**
```json
{
  "answer": "Based on the HR policy document, employees are entitled to...",
  "status": "success"
}
```

#### Example 2: Remote Work Policy

**Input:**
```json
{
  "question": "Can I work remotely? What are the requirements?"
}
```

**Output:**
```json
{
  "answer": "According to the HR policy, remote work is permitted under the following conditions: [detailed policy information]",
  "status": "success"
}
```

### Key Features Demonstrated

✅ **User Interactivity**: RESTful API for real-time Q&A  
✅ **Automation**: Automatic document retrieval and answer generation  
✅ **Business Application**: Solves real HR department challenges  
✅ **Accuracy**: Answers based on actual company policy documents  
✅ **Scalability**: Handles multiple concurrent requests  

---

## 5. Output Screenshots/Results

### API Testing with cURL

```bash
# Health Check
curl http://127.0.0.1:5003/api/v1/
# Response: {"message": "OK", "status": "healthy", ...}

# Ask Question
curl -X POST http://127.0.0.1:5003/api/v1/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the leave policy?"}'
```

### Python Client Example

```python
import requests

response = requests.post(
    "http://127.0.0.1:5003/api/v1/ask",
    json={"question": "What is the HR policy for remote work?"}
)
print(response.json())
```

### Expected Results

- **Response Time**: < 3 seconds per query
- **Accuracy**: Answers based on actual policy documents
- **Availability**: 24/7 automated responses
- **Consistency**: Same question = same accurate answer

---

## 6. Learning Outcomes

### Technical Skills Acquired

1. **RAG Architecture**: Learned to implement Retrieval-Augmented Generation
2. **Vector Databases**: Understood semantic search with ChromaDB
3. **LLM Integration**: Worked with OpenAI GPT models via LangChain
4. **API Development**: Built RESTful APIs with Flask
5. **Document Processing**: Processed PDFs and created embeddings
6. **Python Best Practices**: Clean architecture, separation of concerns

### AI Concepts Understood

- **Embeddings**: How text becomes numerical vectors
- **Semantic Search**: Finding information by meaning, not keywords
- **RAG**: Combining retrieval and generation for accurate AI
- **Prompt Engineering**: Designing effective system prompts
- **Agent Architecture**: Building AI agents with tools and reasoning

### Business Understanding

- **Problem-Solving**: Identified real business pain points
- **Automation**: Understood how AI can automate repetitive tasks
- **ROI**: Recognized value of AI in reducing operational costs
- **User Experience**: Designed for employee-friendly interactions

### Challenges Overcome

1. **Vector Database Setup**: Learned ChromaDB configuration and persistence
2. **Document Chunking**: Optimized chunk size and overlap for better retrieval
3. **Error Handling**: Implemented robust error handling in API
4. **Architecture Design**: Applied clean code principles (Controller-Service pattern)

---


## 7. Future Enhancements

### Potential Improvements

1. **Multi-language Support**: Add support for multiple languages
2. **Conversation History**: Maintain context across multiple questions
3. **Feedback Loop**: Allow users to rate answers for improvement
4. **Analytics Dashboard**: Track common questions and usage patterns
5. **Integration**: Connect with Slack, Teams, or company intranet
6. **Voice Interface**: Add speech-to-text and text-to-speech
7. **Document Updates**: Automatic re-indexing when policies change

---

## 8. Conclusion

This project successfully demonstrates:
- ✅ Practical application of AI (RAG) to solve real business problems
- ✅ Complete end-to-end AI agent implementation
- ✅ User interactivity through RESTful API
- ✅ Automation of repetitive HR tasks
- ✅ Business value through time and cost savings

The HR Policy Q&A Assistant showcases how AI can be applied to create practical, valuable solutions that improve organizational efficiency and employee experience.

---

