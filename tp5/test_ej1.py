import pytest
from ej1 import validator

@pytest.mark.parametrize("a, res",[
    (455, False),
    (40000000, True),
    (3800000, False),
])

def test_validator(a, res):
    assert validator(a) == res