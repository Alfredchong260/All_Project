
# with  会有代码块, 当打开的文件对象用完以后会自动的关闭文件
# 用来偷懒的
with open('hello.txt', mode='r', encoding='utf-8') as f:
    txt = f.read()

    print(txt)

# 3.5以后, open
# 面向对象中的文件操作, 用 open 用的多一点
# 高级开发
