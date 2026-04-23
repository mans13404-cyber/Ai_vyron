from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/app", response_class=HTMLResponse)
def serve_app():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
def chat(msg: Message):
    user = msg.text.lower()

    if "hello" in user:
        return {"reply": "Hello 😄 kaise ho?"}
    elif "name" in user:
        return {"reply": "Mera naam Vyron AI hai 🤖"}
    else:
        return {"reply": "Mujhe samajh nahi aaya 😅"}
