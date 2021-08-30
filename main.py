from enum import Enum
from fastapi import FastAPI
from pororo import Pororo


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello I'm Pororo. what can I do for you?"}

class ModelName(str, Enum):
    korean = "ko"
    english = "en"

mt = Pororo(task="translation", lang="multi")
@app.get("/pororo/translator")
async def translate_text(source: ModelName, target: ModelName, text: str):
    translated = mt(text, src=source, tgt=target)
    return translated


fib = Pororo(task="fib", lang="ko")
@app.get("/pororo/fib")
async def translate_text(text: str):
    fill_in_the_blank = fib(text)
    return fill_in_the_blank
