# 下载nodejs
# 下载 PyExecjs : 自动将js转换成python
# 明文显示
# md5 16位，32位加密方式
# da8775ead2f05dbe396e6546f7ff1ed9  32位加密
# 断点:方便做调试工作
# https://mp.weixin.qq.com/

# selenium为看到即能爬取到，那么以selenium能否爬取js加密过的数据

import execjs

# 实例化一个node对象
node = execjs.get()

# 对js文件进行编译
ctx = node.compile(open('./weixin.js', encoding='utf-8').read())

# 执行js函数
funcName = "getpwd('{}')".format('123456')
pwd = ctx.eval(funcName)
print(pwd)
