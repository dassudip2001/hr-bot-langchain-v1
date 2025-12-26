# # setup_index.py
# import bs4
# from langchain_openai import OpenAIEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma
# from langchain_community.document_loaders import WebBaseLoader

# # Load data
# loader = WebBaseLoader(
#     web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
#     bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("post-content","post-title")))
# )
# docs = loader.load()

# # Chunk
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# splits = splitter.split_documents(docs)

# # Embeddings + vector DB
# embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Chroma.from_documents(
#     splits, 
#     embeddings, 
#     persist_directory="chroma_db"
# )

# print("✔️ Index built — stored in chroma_db/")
