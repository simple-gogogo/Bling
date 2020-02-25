from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from application.users.models import *
from application import db
from application.api.users.schemas import *

# 生成蓝图对象
api_users = Blueprint('api_users', __name__)

# 取用户列表
@api_users.route('/', methods=['GET'])
def index():
    get_users = Users.query.all()
    users_schema = UsersSchema(many=True)
    users = users_schema.dump(get_users)

    return jsonify({'code': 200, 'message': '成功', 'data': users})

# 取单个用户
@api_users.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    one_user = Users.query.get(int(user_id))
    users_schema = UsersSchema() 
    user = users_schema.dump(one_user)

    return jsonify({'code': 200, 'message': '成功', 'data': user})

# 新增用户
@api_users.route('/', methods=['POST'])
def add_user():
    json_data = request.get_json()
    json_data['password'] = generate_password_hash(json_data['password'])
    users_schema = UsersSchema()
    user = users_schema.load(json_data)
    db.session.add(user)
    db.session.commit()
    return jsonify({'code': 200, 'message': '成功', 'data': {'user_id': user.id}})

# 修改用户
@api_users.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    json_data = request.get_json()

    user = Users.query.get(int(user_id))
    if 'password' in json_data:
        user.password = generate_password_hash(json_data['password'])
    if 'username' in json_data:
        user.username = json_data['username']
    if 'mobile' in json_data:
        user.mobile = json_data['mobile']
    db.session.add(user)
    db.session.commit()

    users_schema = UsersSchema()
    user_json = users_schema.dump(user)    
    return jsonify({'code': 200, 'message': '成功', 'data': user_json})    

# 删除用户
@api_users.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get(int(user_id))
    db.session.delete(user)
    db.session.commit()
    return jsonify({'code': 200, 'message': '成功', 'data': {'user_id': user_id}})        



