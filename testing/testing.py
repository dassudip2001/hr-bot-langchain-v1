# # app.py
# from flask import Flask, request, jsonify
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_chroma import Chroma
# from langchain.tools import tool
# from langchain.agents import create_react_agent, AgentExecutor
# from langchain_core.prompts import ChatPromptTemplate

# app = Flask(__name__)

# # ---- Load Vector DB ----
# embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
# vector_store = Chroma(
#     persist_directory="chroma_db",
#     embedding_function=embeddings
# )

# # ---- Retrieval Tool ----
# @tool
# def retrieve(query: str):
#     """Retrieve context from knowledge base"""
#     docs = vector_store.similarity_search(query, k=3)
#     return "\n\n".join(doc.page_content for doc in docs)

# tools = [retrieve]

# # ---- LLM + Agent ----
# llm = ChatOpenAI(model="gpt-4.1-mini")
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "Use the retrieval tool when needed to answer questions."),
#     ("human", "{input}")
# ])

# agent = create_react_agent(llm, tools, prompt)
# executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# # ---- API Route ----
# @app.route("/ask", methods=["POST"])
# def ask():
#     user_q = request.json.get("question", "")
#     if not user_q:
#         return jsonify({"error": "question missing"}), 400

#     result = executor.invoke({"input": user_q})
#     return jsonify({"answer": result["output"]})


# @app.route("/", methods=["GET"])
# def home():
#     return "RAG Flask API is running!"


# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
