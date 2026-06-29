from fastapi import APIRouter
from pydantic import BaseModel
from src.database.crud import select_investment, insert_investment, delete_investment

router = APIRouter()

class Investments(BaseModel):
    date: str
    institution: str
    investment: str
    movement: str
    value: float
    asset_name: str

@router.get("/investments")
def investments():
    """Retorna todos os investimentos cadastrados"""
    return {"investments": select_investment()}

@router.post("/investments")
def create_investiments(expense: Investments):
    """Cria um novo tipo de investimento no banco"""
    insert_investment(expense.date, expense.institution, expense.investment, expense.movement, expense.value, expense.asset_name)

@router.delete("/investments/{id}")
def remove_investments(id: int):
    """Apaga um tipo de investimento do banco pelo id."""
    delete_investment(id)