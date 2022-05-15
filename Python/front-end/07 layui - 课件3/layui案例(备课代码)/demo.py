# -*- coding: utf-8 -*-
# @author: 正心全栈编程
"""

"""
import faker
import random

fake = faker.Faker('zh-cn')

for i in range(1, 101):
    # stu = {
    #     'no': f'{i:0>6}',
    #     'name': fake.name(),
    #     'email': fake.email(),
    #     'gender': random.choice(['男', '女']),
    #     'city': fake.city(),
    # }
    print((f'{i:0>6}', fake.name(), fake.email(), random.choice(['男', '女']), fake.city(), fake.phone_number()))
