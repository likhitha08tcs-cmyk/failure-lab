from fastapi import FastAPI
# import nonexistent_module

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}
