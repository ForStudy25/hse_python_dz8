import datetime

from main import time_converter


def test_time_converter(t: int):
    result = time_converter(t)
    if t < 0:
        buf = datetime.datetime.fromtimestamp(0) - datetime.timedelta(seconds=((-1) * t))
        test_result = buf.strftime('%H:%M:%S %d/%m/%Y')
    else:
        test_result = datetime.datetime.fromtimestamp(t).strftime('%H:%M:%S %d/%m/%Y')
    assert result == test_result

test_time_converter(1735130000)
test_time_converter(0)
test_time_converter(-1)
