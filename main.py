import datetime
import math

from flask import Flask, request

app = Flask(__name__)


def circle_square(r):
    if r < 0:
        return 0
    return math.pi * (r ** 2)


@app.route("/circle_square/<r>")
def route_circle_square(r):
    try:
        r_value = float(r)
        square = circle_square(r_value)
        
        return f"Расчет площади круга с точностью до 2-х знаков.<br>PI * {r_value}^2 = {square:.2f}"
    except Exception as e:
        return f"Возникла ошибка!<br>{e}"
    except:
        return f"Возникла ошибка!"


def convert(rub):
    if rub < 0:
        return 0
    return rub * 0.073


@app.route("/convert/<r>")
def route_convert(r):
    try:
        rub_value = float(r)
        cny_value = convert(rub_value)
        
        return f"Конвертация RUB в CNY.<br>{rub_value} RUB = {cny_value} CNY"
    except Exception as e:
        return f"Возникла ошибка!<br>{e}"
    except:
        return f"Возникла ошибка!"


def time_converter(t):
    if t < 0:
        buf = datetime.datetime.fromtimestamp(0) - datetime.timedelta(seconds=((-1) * t))
        return buf.strftime('%H:%M:%S %d/%m/%Y')
    else:
        return datetime.datetime.fromtimestamp(t).strftime('%H:%M:%S %d/%m/%Y')


@app.route("/time_converter/<t>")
def route_time_converter(t):
    try:
        time_value = int(t)
        date_value = time_converter(time_value)
        return f"Конвертация UNIX Timestamp в дату.<br>{time_value}<br>{date_value}"
    except Exception as e:
        return f"Возникла ошибка!<br>{e}"
    except:
        return f"Возникла ошибка!"


@app.route("/")
def index():
    return "Home"


if __name__== "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
