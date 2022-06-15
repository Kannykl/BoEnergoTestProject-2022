from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from schemas.markov import Probabilities
from services.exceptions import InvalidDegreeException
from services.markov_chain import markov

markov_router = APIRouter()


@markov_router.post("/markov_chain", response_model=Probabilities, status_code=status.HTTP_200_OK)
async def markov_chain(n: int):
    """Returns probability of item colour or raises Exception"""
    try:
        probabilities = markov(n)

    except InvalidDegreeException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Number of item can not be negative number, from 1 to 100"
        )

    return probabilities
