from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/macro')
def macro():
    return render_template('0401macro.html')


@app.route('/extend')
def extend():
    return render_template('0501index.html')


@app.route('/extend2')
def extend2():
    return render_template('0502login.html')


@app.route('/include')
def include():
    return render_template('0601includ.html')


@app.route('/ex_static')
def ex_static():
    name = '正心'
    messages = [
        {'title': '有位非常漂亮的女同事，有天起晚了没有时间化妆便急忙冲到公司。结果那天她被记旷工了……'},
        {'title': '失恋算个啥？轻轻的，你走吧，千万别后悔，因为只要你一挥手，就会发现，已经有那等不及的意中人，正偷偷摸摸拉你的手！'},
        {'title': '世界上最有钱的人是奥特曼，因为所有取款机上都印着他名字的缩写“ATM” 。'},
        {'title': '所谓爱情也不过是：看上了，追求了，好上了，开心了；不久后，腻了，吵了，淡了，散了。'},
        {'title': '据说失眠的同学盯着看十分钟就能睡着了。'},
        {'title': '才知道，朋友就像人民币，有真、也有假，可惜我不是验钞机。'},
        {'title': '回想这几年，尝尽辛酸艰难。从一开始什么都没有到30万，从30万到200万，从200万、300万到现在的1300万！不是炫耀，我只是想通过我自己的经历告诉我的朋友们——手机像素越高，拍的照片越清晰！'},
    ]
    return render_template('0701static.html', name=name, messages=messages)
