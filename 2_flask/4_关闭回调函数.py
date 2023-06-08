from flask import Flask
import atexit

app = Flask(__name__)

def shutdown_callback():
    # 这里可以编写你想要执行的关闭操作或清理代码
    print("Flask应用程序关闭了。")

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    # 注册关闭回调函数
    atexit.register(shutdown_callback)

    # 启动Flask应用程序
    app.run()
