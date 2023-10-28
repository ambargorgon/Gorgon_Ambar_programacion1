import pytest
from ej2 import word_cutter


@pytest.mark.parametrize("a, res",[
    ("La pelota rueda", 5),
    ("La bicicleta verde", 5),
    ("Mosca negra", 5),
])

def test_word_cutter(a, res):
    assert word_cutter(a) == res