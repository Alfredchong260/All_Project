import execjs

# 实例化一个node对象
node = execjs.get()

# 对js文件进行编译
ctx = node.compile(open('./fkw.js', encoding='utf-8').read())

# 执行js函数
funcName = "getpwd('{}')".format('123456')
pwd = ctx.eval(funcName)
print(pwd)
