

print('这是执行的代码逻辑')
print('__name__: ', __name__)


if __name__ == '__main__':  # 在此逻辑下的代码, 仅能够在当前py文件执行; 一旦被其他模块引用,不会执行if代码块的逻辑
    print('if条件成立')