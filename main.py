from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

# Load student data
with open("data.json", "r") as f:
    student_data = json.load(f)

student_dict = {student["name"]: student["marks"] for student in student_data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    marks = [student_dict.get(n, None) for n in name]
    return {"marks": marks}

# To run locally: uvicorn main:app --reload