from flask import Flask

# 测试用例方法以test_开始
def test_app(app):
    # assert表示断言 
    assert isinstance(app, Flask)