import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    HF_TOKEN: str | None = os.getenv("HF_TOKEN")