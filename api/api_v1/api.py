from fastapi import APIRouter
from .endpoints.equation import equation_router
from .endpoints.markov import markov_router

api_router = APIRouter()

api_router.include_router(equation_router, prefix="", tags=["equation"])
api_router.include_router(markov_router, prefix="", tags=["markov"])
