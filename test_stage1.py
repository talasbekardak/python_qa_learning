from stage0 import multiply, is_even, get_max


def test_multiply():
    assert multiply(3, 4) == 12

def test_is_even():
    assert is_even(7) == False
    assert is_even(4)

def test_get_max():
    assert get_max([3,1,8,2]) == 8