# # pip install fastapi pydantic uvicorn python-dotenv

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_history = [{"role": "developer", "content": "You are a helpful chat-bot."}]

class Message(BaseModel):
    user_input: str

# 
@app.post("/chat")
# 
def chat_endpoint(data: Message):
    # 
    user_input = data.user_input

    # 
    chat_history.append({"role": "user", "content": user_input})

    # 
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=chat_history
    )

    # 
    assistant_message = response.choices[0].message.content
    # 
    chat_history.append({"role": "assistant", "content": assistant_message})

    return {"response": assistant_message}
