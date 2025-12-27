from dotenv import load_dotenv
from pydantic import BaseModel
import os
load_dotenv()


class Config(BaseModel):
    app_name: str = "Rabindra Nath Tagore"
    debug: bool = False
    port: int = os.getenv("PORT")
    LANGSMITH_TRACING: bool = False
    LANGSMITH_API_KEY: str = os.getenv("LANGSMITH_API_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

config = Config()