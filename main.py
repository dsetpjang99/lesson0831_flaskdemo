from flask import Flask
from datetime import datetime

app = Flask(__name__)  # __name__ => __main__

books = {1: "Python book", 2: "Java book", 3: "Flask book"}


@app.route("/")
def index():
    today = datetime.now()
    print(today)
    return f"<h1>Hello Flask!<br>{today}</h1>"


@app.route("/books")
def show_books():
    return books


@app.route("/book/<int:id>")
# 在網頁世界的語法中，參數的型態都是預設為string，所以若是要指定型態，需在route內部寫入
def show_book(id):
    # 輸出有書 <h1>第一本書：xxx</h1>
    if id not in books:
        return f"<h2 style='color:red'>無此編號：{id}</h2>"
    return f"<h1>第{id}本書：{books[id]}</h1>"
    # 無此編號
    # return books[id]


@app.route("/sum/x=<x>&y=<y>")
def my_sum(x, y):
    # 參數不正確，請輸入參數錯誤 (try + except)
    try:
        total = eval(x) + eval(y)
        return f"<h1>{x}+{y}={total}</h1>"
    except Exception as e:
        print(e)

    return "<h2>參數不正確！</h2>"


@app.route("/bmi/n=<name>&h=<height>&w=<weight>")
def getbmi(name, height, weight):
    try:
        bmi = round(eval(weight) / ((eval(height) / 100) ** 2), 2)
        print(f"{name},{height}, {weight}, bmi")
        return f"<h1><span style='color:blue'>姓名:{name}</span> BMI:{bmi}</h1>"
    except Exception as e:
        print(e)

    return "<h2>輸入錯誤</h2>"


app.run(debug=True)
