from database import RedisClient
from flask import request #获取地址的查询参数
from flask import jsonify
import flask

app = flask.Flask(__name__)

Client = RedisClient()

# 视图函数
@app.route('/')
def index():
    return '<h2>欢迎来到代理池</h2>'

@app.route('/get')
def one_proxy():
    '''随机获取一个代理，需要调用数据库模块random()方法'''
    proxy = Client.random_proxy()

    return proxy

@app.route('/getcount')
def get_count():
    num = request.args.get('num','')
    if not num: # 如果没有获取到查询参数
        num = 1

    else:
        num = int(num)

    proxies = Client.count_for_num(num)

    return jsonify(proxies)

@app.route('/count')
def count():
    '''获取当前数据库所有代理的数量'''
    proxy_num = Client.count()

    return f"代理池目前还有{proxy_num}个代理可用"

@app.route('/getall')
def getall():
    all_proxies = Client.all()

    return jsonify(all_proxies)

@app.route('/get100')
def getfull():
    proxy = Client.getfullmark()

    return jsonify(proxy)

if __name__ == '__main__':
    # 运行实例化的对象
    app.run(debug=True)
