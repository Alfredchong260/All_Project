import execjs   # 安装名:pyexecjs  导入模块的名字: execjs


"""读取js代码"""
with open('02 百度翻译js解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

"""编译js代码"""
compile_result = execjs.compile(js_code)   # 传入js代码, 编译
print(compile_result)

"""调用js"""
encode_result = compile_result.call('e', '你好')
print(encode_result)

