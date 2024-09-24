from fastapi import FastAPI
from pydantic import BaseModel
import openai

# Initialize FastAPI app
app = FastAPI()

# Define a Pydantic model for request body validation
class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: ChatRequest):
    prompt = request.prompt
    response = openai.Completion.create(
        model="gpt-4", 
        prompt=prompt,
        max_tokens=150
    )
    return {"response": response.choices[0].text}