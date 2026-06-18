# Install Libraries: pip install fastapi uvicorn pydantic

# Execution Command: uvicorn project_delete:app --reload

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json

app = FastAPI()

def load_data():
    with open('student_data.json', 'r') as f:
        data = json.load(f)

    return data



def save_data(data):
    with open('student_data.json', "w") as f:
        json.dump(data, f, indent=4)



@app.get("/")
def hello_world():
    return {"Message": "Student Management System API"}



# DELETE endpoint to remove a student by ID
@app.delete('/delete/{student_id}')
def delete_student(student_id: str):

    # Load existing student data from JSON file
    data = load_data()

    # If the student ID does not exist, raise error
    if student_id not in data:
        raise HTTPException(status_code=404, detail='Student not found')
    
    

    # Remove the student from data
    del data[student_id]

    # Save updated data to the JSON file
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Student deleted successfully'})
