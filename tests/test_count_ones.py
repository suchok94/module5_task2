import pytest
from src.count_ones import count_ones

@pytest.mark.parametrize('value, extend_result', [
    (1, 1),
    (2, 1),
    (47, 5),
    (95, 6)
])
def test_count_ones_positive(value, extend_result):
    assert count_ones(value) == extend_result


@pytest.mark.parametrize('value, extend_result',[
    (0, 0)
])
def test_count_ones_border(value, extend_result):
    assert count_ones(value)== extend_result


@pytest.mark.parametrize('value, extend_result', [
    (-1, pytest.raises(ValueError)),
    ('', pytest.raises(AssertionError))

])
def test_count_ones_negative(value, extend_result):
    with extend_result:
        assert count_ones(value) == extend_result