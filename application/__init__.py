from flask import Flask, request, make_response, redirect, abort, render_template
from flask_script import Manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

# 初始化LoginManager
login_manager = LoginManager()
# 设为'strong'侦测ip地址和user-agent信息有无异常，有异常就登出
login_manager.session_protection = 'strong'
# 指定登录页面
login_manager.login_view = 'users.login'

# 创建数据库连接
db = SQLAlchemy()

# 使用工厂方法创建app，方便测试
def create_app(config=None):
    app = Flask(__name__)
    if config is not None:
        # 加载配置信息
        app.config.from_object(config)

    #注册蓝图对象
    from application.users.views import users
    from application.home.views import home
    from application.projects.views import projects
    from application.api.users.views import api_users

    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(projects, url_prefix='/projects')
    
    app.register_blueprint(api_users, url_prefix='/api/users')

    # 跟app发生关系
    db.init_app(app)
    login_manager.init_app(app)

    return app






