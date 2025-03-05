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


def send_message(message: str):
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
        max_tokens=10240,
        stream=True  # Enable streaming
    )

    full_response = ""  # Store the complete response

    # Stream and print response in real-time
    for chunk in response:
       if hasattr(chunk.choices[0].delta, "content"):
            full_response += chunk.choices[0].delta.content  # Append to response
            print(chunk.choices[0].delta.content, end="", flush=True)
            
    return full_response

if __name__ == "__main__":
    response = send_message('提供東京三日遊行程')
    print(response)
