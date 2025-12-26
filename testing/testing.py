from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentState, create_agent
from dotenv import load_dotenv
import os
import getpass
load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# ---- Load Vector DB ----
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="rag",     # <-- add this
    persist_directory="chroma_db",
    embedding_function=embeddings
)

model = ChatOpenAI(model="gpt-4.1-mini")

@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

tools = [retrieve_context]
# If desired, specify custom instructions
prompt = (
    "You are a helpful assistant that can answer questions about the Opzeze HR Policy."
    "Only answer the user based on the provided context. If the answer is not in the policy, say so ."
)
agent = create_agent(model, tools, system_prompt=prompt)

query = "leave policy"

# result = agent.invoke({"messages": [{"role": "user", "content": query}]})
# print(result)
for step in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()

