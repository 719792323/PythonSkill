from flask import Flask

app = Flask(__name__)


# 普通字符串的返回值是Content-Type: text/html; charset=utf-8
@app.route('/hello')
def hello():
    return 'hello word'


# dict对象返回值是Content-Type: application/json
@app.route("/json")
def json():
    return {"hello": "world"}


# 直接右键运行，点击链接输入路由
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
