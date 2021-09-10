import execjs

node = execjs.get()

ctx = node.compile(open('./cf.js', encoding='utf-8').read())

funcName = "getpwd('{}')".format('123456')
pwd = ctx.eval(funcName)
print(pwd)
