from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load student data
try:
    with open("data.json", "r", encoding="utf-8") as f:
        student_data = json.load(f)
    student_dict = {student["name"]: student["marks"] for student in student_data}
except (FileNotFoundError, json.JSONDecodeError):
    student_dict = {}

@app.get("/api")
def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "No names provided"}
    marks = [student_dict.get(n, None) for n in name]
    return {"marks": marks}