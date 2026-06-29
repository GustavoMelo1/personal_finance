from fastapi import APIRouter
from pydantic import BaseModel
from src.database.crud import select_flow, insert_flow, delete_flow, balance_flow

router = APIRouter()

class Flow(BaseModel):
    date: str
    description:str
    category:str
    type:str
    value:float
    bank:str

@router.get("/expenses")
def flow():
    """Retorna todos os gastos cadastrados"""
    return {"flow": select_flow()}

@router.post("/expenses")
def create_flow(expense: Flow):
    """Cria um novo tipo de gasto no banco"""
    insert_flow(expense.date, expense.description, expense.category, expense.type, expense.value, expense.bank)

@router.get("/expenses/balance")
def balance():
    """Calcula e retorna o saldo atual (ganhos menos gastos)."""
    return {"balance": balance_flow()}

@router.delete("/expenses/{id}")
def remove_flow(id: int):
    """Apaga um tipo de gasto do banco pelo id."""
    delete_flow(id)