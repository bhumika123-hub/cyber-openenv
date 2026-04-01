import os
import requests
from openai import OpenAI

# ================= CONFIG =================
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
API_KEY = os.getenv("OPENAI_API_KEY")

MAX_STEPS = 5

# OpenAI Client
client = OpenAI(
    base_url=os.getenv("API_BASE_URL_LLM", "https://api.openai.com/v1"),
    api_key=API_KEY
)