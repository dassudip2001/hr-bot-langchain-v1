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
    collection_name="rag",
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
    "You are a helpful assistant that can answer questions about the Opzeze HR Policy. "
    "Only answer the user based on the provided context. If the answer is not in the policy, say so."
)

agent = create_agent(model, tools, system_prompt=prompt)

def ask_agent(question: str) -> str:
    """Ask the RAG agent and return string answer."""
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    return result["messages"][-1].content
