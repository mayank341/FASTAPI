# Install Libraries: pip install fastapi uvicorn pydantic

# Execution Command: uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def hello_world():
    return {"Message": "Hello World"}



# @app.get("/about")
# def about():
#     return {"Message": "Welcome to Python_AI Hindi Academy YouTube Channel. Here, you will learn Artificial Intelligence with Python in a very simple and easy-to-understand way."}

