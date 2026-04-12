from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/nowtime")
def now_time():
    now = datetime.now()
    # print(now)
    return now.strftime("%Y-%m-%d %H:%M:%S")


@app.route("/books")
@app.route("/books/id=<int:id>")
def get_books(id=None):
    try:
        books = {1: "Python book", 2: "Java book", 3: "C++ book"}
        if id is None:
            return books
        else:
            return books[id]
    except Exception as e:
        return f"書籍編號錯誤:{e}"


@app.route("/bmi/height=<h>&weight=<w>")
def get_bmi(h, w):
    try:
        bmi = round((eval(w) / (eval(h) / 100) ** 2), 2)
        return f"<h1>身高:{h}m,體重:{w}kg,BMI值為:{bmi}</h1>"
    except Exception as e:
        return f"身高或體重輸入錯誤:{e}"


app.run(debug=True)
