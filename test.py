from math import pi

from main import circle_square

def test_circle_square(r):
    result = circle_square(r)
    if r < 0:
        test_result = 0
    else:
        test_result = pi * (r ** 2)
    assert result == test_result


test_circle_square(9)
test_circle_square(100)
test_circle_square(-12)
