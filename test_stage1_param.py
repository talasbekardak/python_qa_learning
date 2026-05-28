import pytest
from stage0 import multiply, is_even, get_max

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (7, False),
    (0, True),
])
def test_is_even_param(n, expected):
    assert is_even(n) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2,3,6),
    (5,2,10),
    (4,5,20)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("lst, expected", [
    ([5,7,8], 8),
    ([5,9,8], 9),
    ([5,70,8], 70)
])
def test_get_max(lst, expected):
    assert get_max(lst) == expected