from fastapi import FastAPI

# Initialize the application
app = FastAPI()

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello, World!"}
