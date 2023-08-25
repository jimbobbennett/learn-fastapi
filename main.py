import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Messaging",
        "description": "Operations for messages.",
    }
]

app = FastAPI(
      servers=[{"url": "http://127.0.0.1:8000", "description": "dev"}],
      contact={
         "name": "JimBobBennett",
         "url": "https://jimbobbennett.dev"
      },
      description="A test API for LibLab",
      openapi_tags=tags_metadata
   )

class Message(BaseModel):
   message: str

@app.get("/", operation_id="root_message", tags=["Messaging"])
async def root() -> Message:
   '''
   Gets a friendly hello message
   '''
   return {"message": "Hello World"}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)