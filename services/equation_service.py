import math
from numbers import Real
from dataclasses import dataclass


from services.exceptions import ZeroDiscriminantException


@dataclass(slots=True, frozen=True)
class Roots:
    x_1: Real
    x_2: Real | None


def positive_discriminant(discriminant: Real, a: Real, b: Real):
    """Solve equation if discriminant > 0

    :param discriminant:
    :param a:
    :param b:
    :return:
    Roots of equation
    """
    x_1 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
    x_2 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)

    return Roots(
        x_1=x_1,
        x_2=x_2
    )


def zero_discriminant(discriminant: Real, a: Real, b: Real):
    """Solve equation if discriminant equal to 0

    :param discriminant:
    :param a:
    :param b:
    :return:
    Roots of equation
    """
    x_1 = round(-b / (2 * a), 2)

    return Roots(
        x_1=x_1,
        x_2=None
    )


def solver(a: Real, b: Real, c: Real) -> Roots:
    """Solve equation for three discriminant options"""
    discriminant = (b ** 2 - 4 * a * c)

    if discriminant > 0:
        equation_roots = positive_discriminant(discriminant, a, b)

    elif discriminant == 0:
        equation_roots = zero_discriminant(discriminant, a, b)

    else:
        raise ZeroDiscriminantException()

    return equation_roots
