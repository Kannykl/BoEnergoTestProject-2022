from dataclasses import dataclass

import numpy as np

from services.exceptions import InvalidDegreeException


@dataclass(slots=True, frozen=True)
class Probabilities:
    blue_probability: float
    green_probability: float
    red_probability: float


def markov(n: int):
    """Matrix of probabilistic transitions for a Markov chain."""
    if n > 0:
        a = np.array([[.5, .3, .2],
                      [.6, .25, .15],
                      [.55, .3, .15]]
                     )

        probability_matrix = np.linalg.matrix_power(a, n)

        return Probabilities(
            blue_probability=probability_matrix[0][0],
            green_probability=probability_matrix[0][1],
            red_probability=probability_matrix[0][2]
        )

    else:
        raise InvalidDegreeException
