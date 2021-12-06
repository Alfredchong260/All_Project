import datetime

# 扑克牌中的大小比较  3 4 5 6 7 8 9 10 J Q K A 2

# 自定义一套比价规则
weights = {
    '3': 1, '4': 2, '5': 3, '6': 4,
    '7': 5, '8': 6, '9': 7, '10': 8,
    'J': 9, 'Q': 10, 'K': 11, 'A': 12,
    '2': 13
}


class Hearts:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        # 大于符号的运算规则
        return weights[self.value] > weights[other.value]

    def __str__(self):
        return f'<Hearts {self.value}>'


# 单张牌
# 两张牌
# 三张牌
# 三带一
# 三带二
# 四张牌


A = Hearts('A')
K = Hearts('K')
print(A)
print(K)
print('A > K:\t', A > K)
