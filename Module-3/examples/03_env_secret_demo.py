import os
from dotenv import load_dotenv

load_dotenv()

app_env = os.getenv("APP_ENV", "local")
demo_api_key = os.getenv("DEMO_API_KEY")

if not demo_api_key:
    raise RuntimeError("DEMO_API_KEY is missing. Copy .env.example to .env and set a local demo value.")

print("Environment:", app_env)
print("API key configured:", True)
