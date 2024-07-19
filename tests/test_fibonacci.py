import pytest
from src.fibonacci import fibonacci

@pytest.mark.parametrize('value, extend_result',[
    (2, [0, 1, 1]),
    (3, [0, 1, 1, 2]),
    (10, [0, 1, 1, 2, 3,5, 8, 13, 21, 34, 55])
])
def test_fibonacci_positive(value, extend_result):
    assert fibonacci(value) == extend_result

@pytest.mark.parametrize('value, extend_result',[
    (0, [0])
])
def test_fibonacci_border(value, extend_result):
    assert fibonacci(value)== extend_result

@pytest.mark.parametrize('value, extend_result', [
    (-1, pytest.raises(ValueError)),
    ('', pytest.raises(AssertionError))
])
def test_fibonacci_negative(value, extend_result):
    with extend_result:
        assert fibonacci(value) == extend_result


