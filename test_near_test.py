import pytest

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 3),
    (0.1, 0.2, 0.3)
    ])
def test_add(a,b,c):
    from near_test import add
    answer = add(a, b)
    #use approx so you dont have to be Exactly that number. Look up documentation for larger range
    assert pytest.approx(answer) == c