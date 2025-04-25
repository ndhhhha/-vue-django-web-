'''
生成token
使用python 的 pyjwt库进行生成token
1、安装pyjwt库
pip install pyjwt
2、使用方法
import jwt
导入后使用参数为（1）字典、（2）密钥、（3）加密方式
'''
import time
import jwt
from django.conf import settings

def generate_token(data:dict):
    #设置过期时间
    data['exp'] = settings.JWT_EXPIRE + int(time.time())
    #生成token
    token = jwt.encode(data,settings.JWT_SECRET_KEY,algorithm='HS256')
    #返回token
    return token

def verify_token(token):
    #验证token
    try:
        data = jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=['HS256'])
        return data
    # except jwt.ExpiredSignatureError:
    #     return {'code':1,'message':'token已过期'}
    # except jwt.InvalidTokenError:
    #     return {'code':1,'message':'token无效'}
    except Exception:
        return None