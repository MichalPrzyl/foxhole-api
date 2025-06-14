from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from foxholemanager import FoxholeManager

app = FastAPI()

# Dodaj CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # albo ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():

    x = FoxholeManager()
    api_data = x.main()

    return {"data": api_data}

