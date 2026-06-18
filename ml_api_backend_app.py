# Install Libraries: pip install fastapi uvicorn pydantic pandas

# Execution Command (Development): uvicorn ml_api_backend_app:app --reload
# Execution Command (Production): uvicorn ml_app:app --host 0.0.0.0 --port 8000



from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd



app = FastAPI(
    title="Insurance Premium Prediction API",
    description="Predicts insurance premiums using a pre-trained XGBoost model"
)



def load_model():
    try:
        with open('xgboost_insurance_model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    
    except FileNotFoundError:
        raise RuntimeError("Model file 'xgboost_insurance_model.pkl' not found.")
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {str(e)}")

# load lodel
model = load_model()   


# Input schema matching your dataset
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the individual")]

    sex: Annotated[Literal['male', 'female'], Field(..., description="Gender of the individual")]

    bmi: Annotated[float, Field(..., gt=10, lt=60, description="Body Mass Index")]

    children: Annotated[int, Field(..., ge=0, le=20, description="Number of children")]

    smoker: Annotated[Literal['yes', 'no'], Field(..., description="Smoking status")]

    region: Annotated[Literal['southwest', 'southeast', 'northwest', 'northeast'], Field(..., description="Region")]



    @computed_field
    @property
    def bmi_category(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "normal"
        elif bmi < 30:
            return "overweight"
        else:
            return "obese"



    @computed_field
    @property
    def smoking_risk(self) -> str:
        if self.smoker == 'yes' and self.bmi > 30:
            return "high"
        elif self.smoker == 'yes' or self.bmi > 27:
            return "medium"
        else:
            return "low"



# Prediction endpoint
@app.post("/predict")
async def predict_premium(data: UserInput):
    try:
        # Prepare DataFrame with all required columns, including computed fields
        input_df = pd.DataFrame([{
            "age": data.age,  # Ensure int

            "sex": data.sex,  # Keep as categorical

            "children": data.children,  # Ensure int

            "region": data.region,  # Keep as categorical

            "bmi_category": data.bmi_category,  # Include computed field
            "smoking_risk": data.smoking_risk  # Include computed field
        }])



        # Define expected columns (based on model training)
        expected_columns = [
            'age', 'sex', 'children','region', 'bmi_category', 'smoking_risk'
        ]

        # Check for missing columns
        missing_cols = [col for col in expected_columns if col not in input_df.columns]
        if missing_cols:
            raise ValueError(f"Columns are missing: {missing_cols}")

        # Reorder columns to match model expectations
        input_df = input_df[expected_columns]



        # Predict
        prediction = model.predict(input_df)[0]

        # Return result with only the predicted value
        return JSONResponse(status_code=200, content={
            "predicted_amount": float(prediction)  # Ensure JSON compatibility
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

