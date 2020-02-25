SECRET_KEY = '23431343DEWQERsadfdsHwer&^23cA'
# 设置数据库连接字符串
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Vff123456@127.0.0.1/irest_test?charset=UTF8MB4'
# 不跟踪修改，不设置会有警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False

DEBUG = True
TESTING = True
WTF_CSRF_ENABLED = False
