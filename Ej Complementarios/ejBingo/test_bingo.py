import pytest
from functions import *

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
matrix_hor = [[1,2,3,4,5],["X","X","X","X","X"],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
matrix_ver =  [[1,"X",3,4,5],[6,"X",8,9,10],[11,"X",13,14,15],[16,"X",18,19,20],[21,"X",23,24,25]]
matrix_diag = [["X",2,3,4,5],[6,"X",8,9,10],[11,12,"X",14,15],[16,17,18,"X",20],[21,22,23,24,"X"]]

ret_matrix1= [[1,2,3,4,5],[6,7,8,9,10],[11,12,"X",14,15],[16,17,18,19,20],[21,22,23,24,25]]
ret_matrix2 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,"X",14,15],[16,17,18,19,20],[21,22,23,24,"X"]]
### MATCH NUMERO RANDOM ### 
@pytest.mark.parametrize("a, b, res",[
    (13, matrix, ret_matrix1),
    (62, matrix, matrix),
    (25, matrix, ret_matrix2),
])

def test_random_validator(a,b, res):
    assert random_validator(a,b) == res

### FILA HORIZONTAL ###

@pytest.mark.parametrize("a, res",[
    (matrix_hor, True),
    (matrix_ver, False),
    (matrix_hor, True),
])

def test_row_validator(a, res):
    assert row_validator(a) == res

### FILA VERTICAL ###

@pytest.mark.parametrize("a, res",[
    (matrix_ver, True),
    (matrix, False),
    (matrix_ver, True),
])

def test_column_validator(a, res):
    assert column_validator(a) == res

### FILA DIAGONAL ###

@pytest.mark.parametrize("a, res",[
    (matrix_diag, True),
    (matrix, False),
    (matrix_diag, True),
])

def test_diagonal_validator(a, res):
    assert diagonal_validator(a) == res