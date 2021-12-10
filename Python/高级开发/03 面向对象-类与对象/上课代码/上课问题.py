# __name__ 魔法变量,输出的是代码运行的文件
# __name__ 如果是从当前文件启动,输出的就是 __main__
import db

if __name__ == '__main__':
    print(__name__)
    person = db.Person()
    print(person)
