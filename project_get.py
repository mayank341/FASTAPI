# Install Libraries: pip install fastapi uvicorn pydantic

# Execution Command: uvicorn project_get:app --reload

from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('student_data.json', 'r') as f:
        data = json.load(f)

    return data




@app.get("/")
def hello_world():
    return {"Message": "Student Management System API"}



@app.get("/about")
def about():
    return {"Message": "A fully functional API to manage your student records."}



@app.get("/view")
def view():
    data = load_data()

    return data



@app.get("/student/{student_id}")
def view_student(student_id:str = Path(..., description='Please enter ID of student in records', example='S001')):
    #  = Path(..., description='Please enter ID of student in records', example='S001')

    # load all students
    data = load_data()

    if student_id in data:
        return data[student_id]
    else:
        # return {'Error Message': 'Student not found, Please enter correct student id'}
        raise HTTPException(status_code=404, detail='Student not found, Please enter correct student id')





@app.get("/sort")
def sort_students(
    sort_by: str = Query(..., description="Sort on the basis of age etc."), 
    order_by: str = Query('asc', description="Sort in asc or desc order")):

    # all valid fields (integer or float)
    valid_fields = ['age', ]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}")
    
    if order_by not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")

    data = load_data()

    sort_order = True if order_by == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data






