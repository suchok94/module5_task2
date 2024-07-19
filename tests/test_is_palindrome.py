import pytest
from src.is_palindrome import is_palindrome

@pytest.mark.parametrize('value, extend_result', [
    (121, True),
    (-121, False),
    (10, False)
])
def test_count_ones_positive(value, extend_result):
    assert is_palindrome(value) == extend_result


@pytest.mark.parametrize('value, extend_result',[
    (0, True),
    (1, True)
])
def test_count_ones_border(value, extend_result):
    assert is_palindrome(value)== extend_result


@pytest.mark.parametrize('value, extend_result', [
    ('', pytest.raises(AssertionError))

])
def test_count_ones_negative(value, extend_result):
    with extend_result:
        assert is_palindrome(value) == extend_result