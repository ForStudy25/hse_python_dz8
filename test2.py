from main import convert


def test_convert(r):
    result = convert(r)
    if r < 0:
        test_result = 0
    else:
        test_result = r * 0.073
    assert result == test_result


test_convert(100)
test_convert(0)
test_convert(-100)
