import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Turn the user's request into a short, vivid image generation prompt."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


def image_gen(prompt: str):
    result = client.images.generate(model="gpt-image-1", prompt=prompt)
    image_bytes = base64.b64decode(result.data[0].b64_json)
    with open("output.png", "wb") as f:
        f.write(image_bytes)


if __name__ == "__main__":
    image_gen_prompt = llm("졸업식 캡을 쓴 강아지")
    image_gen(image_gen_prompt)
