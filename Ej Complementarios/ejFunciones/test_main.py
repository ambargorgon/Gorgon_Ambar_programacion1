import pytest
from funciones import digits_sum

@pytest.mark.parametrize("a, res",[
    (100, 1),
    (22, 4),
    (38, 11),
])

def test_digits_sum(a, res):
    assert digits_sum(a) == res