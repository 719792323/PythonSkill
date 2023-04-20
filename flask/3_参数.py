from flask import Flask, request

app = Flask(__name__)


# 接收restful参数
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


# get请求，url参数
# url：user?name=alice&age=13
@app.route('/user', methods=['GET'])
def user_get():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'Name: {name}, Age: {age}'

# 注意发送的请求要是Content-Type:application/json，否则request.get_json()会报错
# post请求，body参数
@app.route('/user', methods=['POST'])
def user_post():
    data = request.get_json()
    name = data['name']
    age = data['age']
    return f'Name: {name}, Age: {age}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
