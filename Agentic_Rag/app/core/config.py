from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    HF_TOKEN: str | None = os.getenv("HF_TOKEN")
    