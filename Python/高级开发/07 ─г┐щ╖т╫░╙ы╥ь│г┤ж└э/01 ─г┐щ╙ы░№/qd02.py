"""
    模块: 所有的 py 都是一个模块

"""
# 1. 直接导入一整个模块
import qd01 as q1  # as 起一个别名

print(q1)
# 使用方式 模块名.属性
print(q1.pi)
print(q1.Circle)
# 模块名.对象
c1 = q1.Circle(4)
c2 = q1.Circle(5)
# 模块名.方法
c3 = q1.add(c1, c2)
print(c3)
