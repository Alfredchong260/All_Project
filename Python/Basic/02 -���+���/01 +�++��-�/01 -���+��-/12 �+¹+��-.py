"""
布尔类型: 极端
    这个数据类型只有两种结果, 要么是 True(真/对) 要么是 False(假/错)
    bool 指布尔类型
"""
# True  才是布尔类型的关键字, true只是一个变量名
# False

true = True

print(true)
print(type(true))


false = False

print(false)
print(type(false))


"""布尔类型的隐式转换"""
print('----------------------------------------------------')

# 布尔类型需要注意隐式转换
# 隐式转换, 在所有流程控制(判断 循环)中都会进行隐式转换
print(0 > 5)
print(0 < 5)

print('=========================================================')
# 数值类型  除了0以外布尔值全部是 True  <非0即真>
print(bool(0))
print(bool(1))
print(bool(-1))


print('=========================================================')
# 字符串类型: 除了空字符串以外, 其他字符串布尔值都是 True  <非空即真>
print(bool(''))
print(bool('1'))
print(bool('dahkfdh'))
print(bool(' '))

if '123':  # 判断的就是 '123' 的布尔值
    print('123字符布尔值为真')





