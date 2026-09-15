import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def image_gen(prompt: str):
    result = client.images.generate(model="gpt-image-1", prompt=prompt)
    image_bytes = base64.b64decode(result.data[0].b64_json)
    with open("output.png", "wb") as f:
        f.write(image_bytes)


if __name__ == "__main__":
    image_gen("a cute red panda wearing a tiny hat")
