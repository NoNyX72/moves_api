from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Movies API готов к работе!"}