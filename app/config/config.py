from dotenv import load_dotenv
from pydantic import BaseModel
import os
load_dotenv()


class Config(BaseModel): # type: ignore
    app_name: str = "Rabindra Nath Tagore"
    debug: bool = False
    port: int = os.getenv("PORT") # type: ignore
    LANGSMITH_TRACING: bool = False
    LANGSMITH_API_KEY: str = os.getenv("LANGSMITH_API_KEY") # type: ignore
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY") # type: ignore

config = Config()