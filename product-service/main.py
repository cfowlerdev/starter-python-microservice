from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main_route():
    return {"message": "hello world from inventory-service"}
