"""
api服务模块
"""
from configure import SERVER_DEBUG
from database import RedisClient
from flask import request # 从地址获取参数
from flask import jsonify # 把对象转换成字符串
import flask

REDIS = RedisClient()

# __name__ 属于一般写法
app = flask.Flask(__name__)

# 视图函数，提供服务接口 http://demo.spiderpy.cn/get/
@app.route('/') # 装饰器
def index():
    return '<h2>欢迎来到代理池<h2>'

@app.route('/get') # 装饰器
def random_proxy():
    '''随机获得一个代理'''
    proxy = REDIS.random()
    return proxy

@app.route('/getcount') # 装饰器
# 如何取值
def get_proxy():
    '''获取指定数量的代理'''
    num = request.args.get('num', '')
    # 有可能用户没有输入查询参数
    # 所以需要检测用户是否有输入参数
    if not num:
        num = 1
    else:
        num = int(num)

    proxies = REDIS.count_for_num(num)
    return jsonify(proxies)

@app.route('/num') # 装饰器
def get_all():
    '''获取所有代理的数量'''
    count = REDIS.count()
    return f"代理池还剩{count}可用"

@app.route('/all') # 装饰器
def get_num():
    '''获取所有代理'''
    all_proxy = REDIS.all()
    return jsonify(all_proxy)

@app.route('/get100')
def get100():
    proxy = REDIS.get100Proxy()
    return jsonify(proxy)

if __name__ == '__main__':
    app.run(debug=SERVER_DEBUG)
