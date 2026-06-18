# Insurance Premium Prediction System

## 📌 Project Overview

The **Insurance Premium Prediction System** is a Machine Learning-powered web application that analyzes insurance datasets and predicts insurance premiums based on user inputs. The project demonstrates complete **CRUD Operations**, **Data Analysis**, **Machine Learning Model Development**, and **Full-Stack Deployment** using modern technologies.

This project was developed to understand the end-to-end workflow of Data Science and Machine Learning applications, from data preprocessing and model training to API development and frontend integration.

---

## 🚀 Features

### 🔹 CRUD Operations

* Create new insurance records
* Read and retrieve insurance data
* Update existing records
* Delete insurance records
* RESTful API implementation using FastAPI

### 🔹 Data Analysis

* Exploratory Data Analysis (EDA)
* Data Cleaning and Preprocessing
* Feature Engineering
* Statistical Analysis
* Data Visualization

### 🔹 Machine Learning

* Insurance Premium Prediction
* Model Training using XGBoost
* Feature Selection
* Model Evaluation and Performance Analysis
* Prediction API Integration

### 🔹 Interactive Frontend

* User-friendly interface using Streamlit
* Real-time premium prediction
* Dynamic input forms
* Instant results display

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python
* Pydantic
* Uvicorn

### Machine Learning

* XGBoost
* Scikit-Learn
* Pandas
* NumPy

### Frontend

* Streamlit

### Data Visualization

* Matplotlib
* Seaborn

### Database

* JSON / CSV Dataset Storage

---

## 📂 Project Structure

```bash
Insurance-Premium-Predictor/
│
├── data/
│   └── insurance.csv
│
├── models/
│   └── insurance_model.pkl
│
├── backend/
│   ├── main.py
│   ├── schemas.py
│   └── crud.py
│
├── frontend/
│   └── app.py
│
├── notebooks/
│   └── insurance_analysis.ipynb
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Model Training using XGBoost
7. Model Evaluation
8. Model Serialization
9. API Development with FastAPI
10. Frontend Integration with Streamlit

---

## 📊 Model Performance

The XGBoost model was trained on the insurance dataset to predict insurance premiums based on factors such as:

* Age
* BMI
* Smoking Status
* Gender
* Number of Children
* Region

Evaluation metrics used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

## 🔗 API Endpoints

| Method | Endpoint      | Description               |
| ------ | ------------- | ------------------------- |
| GET    | /             | Home Route                |
| GET    | /records      | Get All Records           |
| POST   | /records      | Create Record             |
| PUT    | /records/{id} | Update Record             |
| DELETE | /records/{id} | Delete Record             |
| POST   | /predict      | Predict Insurance Premium |

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Insurance-Premium-Predictor.git
cd Insurance-Premium-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Backend

```bash
uvicorn main:app --reload
```

### Run Streamlit Frontend

```bash
streamlit run app.py
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

* CRUD Operations using FastAPI
* REST API Development
* Data Cleaning and Analysis
* Exploratory Data Analysis (EDA)
* Machine Learning Model Development
* XGBoost Implementation
* Model Deployment Concepts
* Streamlit Application Development
* Backend-Frontend Integration
* End-to-End ML Project Workflow

---

## 📈 Future Improvements

* Database Integration (MongoDB/PostgreSQL)
* User Authentication
* Model Monitoring
* Cloud Deployment
* Docker Containerization
* CI/CD Pipeline

---

## 👨‍💻 Author

**Mayank Kumar**

B.Tech Information Technology Student
Machine Learning & Full Stack Development Enthusiast

GitHub: https://github.com/mayank341

---

## 📄 License

This project is developed for educational and learning purposes.

