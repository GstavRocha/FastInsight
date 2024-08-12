from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def execute_api():
    return {"detail":"Api Running"}
