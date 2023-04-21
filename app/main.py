from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get('/')
def home():
 return "ok"

app.include_router(router)