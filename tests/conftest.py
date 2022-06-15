import pytest


@pytest.fixture
def valid_coefficients():
    return {
            "coefficients": {
                "a": 1,
                "b": 11,
                "c": 0
            }
        }
