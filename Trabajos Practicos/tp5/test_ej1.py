import pytest
from ej1 import validator

#Correr test con "pytest -s"

@pytest.mark.parametrize("a, res",[
    (455, False),
    (40000000, True),
    (3800000, True),
    (1, False)
])

def test_validator(a, res):
    assert validator(a) == res