from flask import get_flashed_messages
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from application.users.models import *

# 测试注册方法
def test_users_register(client):
    # get协议方法测试
    response = client.get('/users/register')
    assert response.status_code == 200
    assert '欢迎注册' in bytes.decode(response.data)

    # post方法测试
    data = {'username': '任铠', 'password': '123456', 'mobile': '12345678901'}
    response = client.post('/users/register', data=data)
    # 判断是否跳转
    assert response.status_code == 302
    assert len(get_flashed_messages()) == 1
    assert '登录成功' in get_flashed_messages()[0]

    # assert '我的项目' in bytes.decode(response.data)

    # 判断用户是否已经添加
    user = Users.query.filter_by(username='任铠').first()
    assert user.password != '123456'
    assert check_password_hash(user.password, '123456')

    # 判断current_user是否正确
    assert current_user.username == '任铠'

# 测试登录失败的情况
def test_users_login(client):
    response = client.get('/users/login')
    assert response.status_code == 200

    data = {'username': '  ', 'password': '123456'}
    response = client.post('/users/login', data=data)
    get_flashed_messages()
    html = bytes.decode(response.data)
    assert '用户名不能为空' in html

    data = {'username': '任铠', 'password': '123456'}
    response = client.post('/users/login', data=data)
    assert response.status_code == 302
    get_flashed_messages()
    assert current_user.username == '任铠'

    data = {'username': '任铠', 'password': '654321'}
    response = client.post('/users/login', data=data)
    assert '用户名或密码错误' in ''.join(get_flashed_messages())

    data = {'username': '任铠 ', 'password': '123456 '}
    response = client.post('/users/login', data=data)
    assert response.status_code == 302
