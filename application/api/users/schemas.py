from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from application.users.models import *
from application import db

# 定义Users model到marshmallow的映射 
# model -> json   json -> model
class UsersSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Users
        sqla_session = db.session

    # id是自动生成的，不需要客户端传给我们，所以只需要从Model序列化成json
    # dump_only=True读取操作，不是写入操作
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    mobile = fields.String(required=True) 
    # 只允许从json序列化成model
    password = fields.String(load_only=True) 
       