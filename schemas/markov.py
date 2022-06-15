from pydantic import BaseModel


class Probabilities(BaseModel):
    """Probabilities of items colour"""
    blue_probability: float
    green_probability: float
    red_probability: float
