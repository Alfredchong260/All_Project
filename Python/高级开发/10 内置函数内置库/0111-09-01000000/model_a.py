def add(x, y):
    return x + y


# 测试结果
# 被当做模块导入的时候不运行下面的代码
# 如果从当前文件运行有又会启动
print('model_a -> __name__:\t', [__name__])  # __name__ 魔法变量
if __name__ == '__main__':
    print('测试结果:\t', add(4, 5))
"""
造轮子的时候会用到,不造轮子就不会用
"""
