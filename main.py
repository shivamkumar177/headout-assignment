from fastapi import FastAPI
from app.routers import read_file

app = FastAPI()

app.include_router(read_file.router)

@app.get('/', status_code=200)
def health():
    return {""}