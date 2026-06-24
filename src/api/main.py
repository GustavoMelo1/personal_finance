from fastapi import FastAPI
from pydantic import BaseModel
from src.database.crud import select_flow, select_investment, select_wishes

app = FastAPI()

class Flow(BaseModel):
    date: str
    description:str
    category:str
    type:str
    bank:str
    value:float

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/expenses")
def flow():
    return {"flow": select_flow()}

@app.post("/expenses")
def create_flow(expense: Flow):
    pass

@app.get("/investments")
def investments():
    return {"investments": select_investment()}

@app.get("/wishes")
def wishes():
    return {"wishes": select_wishes()}

