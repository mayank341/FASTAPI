# Install Libraries: pip install fastapi uvicorn pydantic

# Execution Command: uvicorn project_put:app --reload


from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()



def load_data():
    with open('student_data.json', 'r') as f:
        data = json.load(f)

    return data



def save_data(data):
    with open('student_data.json', "w") as f:
        json.dump(data, f, indent=4)



# Creating Pydantic model for updating student data
# All fields are optional, so only selected fields can be modified using PUT request
class ModifyStudent(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]

    age: Annotated[Optional[int], Field(default=None, gt=0)]

    city: Annotated[Optional[str], Field(default=None)]

    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]

    student_class: Annotated[Optional[str], Field(default=None)]

    marks: Annotated[Optional[int], Field(default=None, ge=0, le=100)]



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



# PUT endpoint to modify existing student data
@app.put('/modify/{student_id}')
def modify_student(student_id: str, modified_student: ModifyStudent):

    # Load current student data from JSON file
    data = load_data()

    # If student ID not found, return 404 error
    if student_id not in data:
        raise HTTPException(status_code=404, detail='Student not found')



    # 1. Get existing student record
    existing_student_info = data[student_id]

    # 2. Extract only the fields provided in update request
    modified_student_info = modified_student.model_dump(exclude_unset=True)

    # 3. Update old data with new values
    for key, value in modified_student_info.items():
        existing_student_info[key] = value

    # 4. Recreate pydantic object to recompute division and result
    existing_student_info['id'] = student_id
    student_pydantic_obj = ModifyStudent(**existing_student_info)

    # 5. Convert pydantic object back to dict (excluding id)
    existing_student_info = student_pydantic_obj.model_dump(exclude=["id"])

    # 6. Save modified dict back to main data
    data[student_id] = existing_student_info

    # 7. Save modified data to the JSON file
    save_data(data)



    return JSONResponse(status_code=200, content={'message': 'Student modified successfully'})
