import pytest
from src.factorial import factorial

@pytest.mark.parametrize('value, extend_result',[
    (1, 1),
    (5, 120)
])
def test_factorial_positive(value, extend_result):
    assert factorial(value)== extend_result

@pytest.mark.parametrize('value, extend_result',[
    (0, 1)
])
def test_factorial_border(value, extend_result):
    assert factorial(value)== extend_result

@pytest.mark.parametrize('value, extend_result', [
    (-1, pytest.raises(ValueError)),
    (21, pytest.raises(ValueError)),
    ('2', pytest.raises(TypeError))
])
def test_factorial_negative(value, extend_result):
    with extend_result:
        assert factorial(value) == extend_result