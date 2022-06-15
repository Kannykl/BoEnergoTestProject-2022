from fastapi import APIRouter
from fastapi import Body
from fastapi import HTTPException
from fastapi import status

from schemas.equation import Coefficients
from schemas.equation import Roots
from services.equation_service import solver
from services.exceptions import ZeroDiscriminantException

equation_router = APIRouter()


@equation_router.post("/solve_equation", response_model=Roots, status_code=status.HTTP_200_OK)
async def solve_equation(coefficients: Coefficients = Body(..., embed=True)):
    """Returns root of equation, throws Exception if discriminant less than zero"""
    try:
        equation_roots = solver(coefficients.a, coefficients.b, coefficients.c)

    except ZeroDiscriminantException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Discriminant less then zero,"
                   "try again with other coefficients"
        )

    return equation_roots
