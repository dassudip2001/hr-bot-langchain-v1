# setup_index.py
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
import os
from dotenv import load_dotenv
import getpass
load_dotenv()




if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Load data
pdf_path= Path(__file__).parent / "../IIA HR Policy.pdf"
loader = PyPDFLoader(pdf_path)
docs = loader.load()

# print("✔️ PDF loaded",docs)

# # Chunk
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
     chunk_overlap=200,
    separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
)
splits = splitter.split_documents(docs)


# # Embeddings + vector DB
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

Chroma.from_documents( # type: ignore
    splits, 
    embeddings, 
    persist_directory="chroma_db",
    collection_name='hr_policy'
)

print("✔️ Index built — stored in chroma_db/")
