# agent_core.py
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
import os

load_dotenv()

# --- Vector DB & Model ---
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="hr_policy",
    persist_directory="chroma_db",
    embedding_function=embeddings
)

model = ChatOpenAI(model="gpt-4.1-mini")

# --- Retrieval Tool ---
@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=3)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

tools = [retrieve_context]

prompt = (
    """You are an AI assistant for answering questions strictly about the Human Resource Policy.

RULES (VERY IMPORTANT):
- You must answer ONLY using the provided policy context.
- If the question is NOT related to Human Resource Policy, you MUST respond exactly with:
  "This question is outside the scope of the Human Resource Policy."
- If the question IS about HR Policy but the answer is NOT present in the provided context, respond exactly with:
  "The requested information is not available in the Human Resource Policy."
- DO NOT use general knowledge.
- DO NOT answer math, programming, general facts, or reasoning questions.
- DO NOT guess or infer.

Follow these rules strictly."""

)

agent = create_agent(model, tools, system_prompt=prompt)

def ask_agent(question: str) -> str:
    """Ask the RAG agent and return string answer."""
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return result["messages"][-1].content
