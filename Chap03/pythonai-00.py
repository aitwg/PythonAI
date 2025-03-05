import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
BASE_URL = os.getenv("BASE_URL")

if not OPENAI_API_KEY:
    raise ValueError("API_KEY environment variable not set.")
if not MODEL_NAME:
    raise ValueError("MODEL_NAME environment variable not set.")
# BASE_URL is optional; if not set, openai library will use the default

client = OpenAI(api_key=OPENAI_API_KEY, base_url=BASE_URL)


def send_message(message: str) -> str:
    """Sends a message to LLM.
    Args:
        message: The message string to send.

    Returns:
       response from LLM
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f'{message}'},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(send_message('Tell me a joke!'))
