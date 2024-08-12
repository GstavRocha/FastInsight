from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def execute_api():
    return ["API IS RUNNING"]