from pydantic import BaseModel


class Coefficients(BaseModel):
    """Coefficients of equation"""
    a: float
    b: float
    c: float


class Roots(BaseModel):
    """Roots of equation"""
    x_1: float
    x_2: float | None

