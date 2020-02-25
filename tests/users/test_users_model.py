from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import sqlalchemy
import pytest
from application.users.models import Users

def test_create_user(session):
    user = Users()
    
    assert user.id is None

    user.username = '黄雄进'
    user.password = generate_password_hash('123456')
    user.mobile = '12341234312'
    session.add(user)
    session.commit()

    assert Users.query.count() == 1
    assert user.id is not None

    db_user = Users.query.get(user.id)

    assert check_password_hash(db_user.password, '123456')

    # 测试用户名是否唯一
    user2 = Users()
    user2.username = '黄雄进'
    user2.password = generate_password_hash('123456')
    user2.mobile = '12341234312'

    try:
        session.add(user2)
        session.commit()
    except Exception as e:
        session.rollback()

    assert Users.query.count() == 1
