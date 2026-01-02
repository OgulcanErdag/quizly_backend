import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

key = os.getenv("GEMINI_API") or os.getenv("GEMINI_API_KEY")
print("Key loaded:", bool(key))

client = genai.Client(api_key=key)

models = client.models.list()
for m in models:
    print(m.name, getattr(m, "supported_generation_methods", None))
