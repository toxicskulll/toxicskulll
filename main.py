from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = [
    "It's not a bug. It's a feature.",
    "Keep calm and grep -r.",
    "Semicolons are just spicy commas.",
    "You miss 100% of the bugs you don't debug.",
    "Coffee is my compiler.",
]

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}
