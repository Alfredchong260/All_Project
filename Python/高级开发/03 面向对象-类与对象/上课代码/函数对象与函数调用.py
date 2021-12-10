"""
    人:
        属性: 名字,身高,体重 ....
        行为: 吃饭/喝酒/打招呼 ...
"""


def eat():
    print('正在吃饭')
    return None


# 能够区分吗?
ear_2 = eat  # --> eat
ear_3 = eat()  # --> None

print(ear_2())  # eat()
print(ear_3())  # None()
