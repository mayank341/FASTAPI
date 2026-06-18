
# Install Libraries: pip install fastapi uvicorn pydantic

# Execution Command: uvicorn project_post:app --reload

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()

def load_data():
    with open('student_data.json', 'r') as f:
        data = json.load(f)

    return data



def save_data(data):
    with open('student_data.json', "w") as f:
        json.dump(data, f, indent=4)



# Creating Pydantic model for input student data validation
class Student(BaseModel):
    id: Annotated[str, Field(..., description="ID of the student", examples=["S001"])]

    name: Annotated[str, Field(..., description="Full name of the student", examples=["Aryan Gupta"])]

    age: Annotated[int, Field(..., gt=5, lt=100, description="Age of the student", examples=[16])]

    city: Annotated[str, Field(..., description="City where the student resides", examples=["Mumbai"])]

    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="Gender of the student")]

    student_class: Annotated[str, Field(..., description="Class/Grade of the student", examples=["10"])]

    marks: Annotated[int, Field(..., ge=0, le=100, description="Marks obtained out of 100", examples=[88])]


    # Compute division based on marks
    @computed_field
    @property
    def division(self) -> str:
        if self.marks >= 60:
            return "First"
        elif self.marks >= 45:
            return "Second"
        elif self.marks >= 33:
            return "Third"
        else:
            return "Fail"


    # Compute result based on division
    @computed_field
    @property
    def result(self) -> str:
        if self.division in ["First", "Second", "Third"]:
            return "Pass"
        else:
            return "Fail"



@app.get("/")
def hello_world():
    return {"Message": "Student Management System API"}



@app.post("/insert")
def add_student(student: Student):
    # Load existing data from file
    data = load_data()

    # Check if the student already exists
    if student.id in data:
        raise HTTPException(status_code=400, detail="Student already exists")



    #converting pydantic datatype of new student into dictionary datatype
    # Adding new student to the database (excluding the id from body)
    data[student.id] = student.model_dump(exclude=["id"])

    # Save updated data back to file
    save_data(data)

    return JSONResponse(status_code=201, content={"Message": "Student added successfully"}
    )
