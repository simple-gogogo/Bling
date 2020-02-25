import pytest
from application import create_app, db as database

# 准备app
@pytest.fixture(scope='session')
def app():
    app = create_app('test_settings')
    return app

# 准备db, session表示该fixuture只在所有测试开始的时候创建一次
@pytest.fixture(scope='session')
def db(app, request):
    database.app = app
    database.create_all()

    # 销毁方法，在测试执行完成后
    def teardown():
        database.drop_all()

    request.addfinalizer(teardown)
    return database

# 准备数据库session
@pytest.fixture(scope='function')
def session(db, request):
    session = db.create_scoped_session()
    db.session = session

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session





