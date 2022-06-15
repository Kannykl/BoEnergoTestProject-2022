import pytest

from main import app
from schemas.equation import Roots
from services.equation_service import solver
from services.exceptions import ZeroDiscriminantException
from fastapi.testclient import TestClient


test_client = TestClient(app=app)


@pytest.mark.parametrize(
    "a,b,c,result",
    (
        (
            1,
            11,
            0,
            Roots(x_1=0.0, x_2=-11.0),
        ),
        (
            4,
            -2,
            0,
            Roots(x_1=0.5, x_2=0.0),
        ),
        (
            -3,
            7,
            0,
            Roots(x_1=-0.0, x_2=2.33),
        ),
        (16, -8, 1, Roots(x_1=0.25, x_2=None)),
    ),
)
def test_solve_equation(a: float, b: float, c: float, result: Roots):
    """Test solve equation with discriminant >=0"""
    result_ = solver(a, b, c)

    assert result_.x_1 == result.x_1
    assert result_.x_2 == result.x_2


@pytest.mark.parametrize(
    "a,b,c",
    (
        (
            9,
            -6,
            2,
        ),
    ),
)
def test_solve_equation_with_exception(a: float, b: float, c: float):
    """Test solve equation with discriminant less than zero"""

    with pytest.raises(ZeroDiscriminantException):
        solver(a, b, c)


def test_solve_equation_endpoint(valid_coefficients):
    """Test endpoint with valid data"""
    response = test_client.post(
        "api/v1/solve_equation", json=valid_coefficients
    )
    assert response.status_code == 200
    assert response.json() == {
                          "x_1": 0.0,
                          "x_2": -11.0
                        }
