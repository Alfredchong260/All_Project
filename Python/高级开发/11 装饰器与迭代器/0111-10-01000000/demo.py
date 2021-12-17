class User:

    def __init__(self, family_name, name):
        self.family_name = family_name
        self.name = name

    @property
    def username(self):
        return self.family_name + self.name

    @username.setter
    def username(self, value):
        self.family_name = value[0]
        self.name = value[1]

    @username.deleter
    def username(self):
        print('可以执行删除的逻辑')


user = User('正', "心")

print(user.username)
user.username = '丸子'
print(user.username)
print(user.family_name)
del user.username
