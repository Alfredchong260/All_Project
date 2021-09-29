# 4. 需要记录学生的 姓名、语文成绩、数学成绩、英语成绩 、总分 (input 学生信息怎么存储?)

name = input('请输入学生姓名:')
chinese = int(input('请输入学生语文成绩:'))
math = int(input('请输入学生数学成绩:'))
english = int(input('请输入学生英语成绩:'))
total =  chinese + math + english

# 用到数据容器?  用哪种?
# 1. 方便取值, 字典<可以存储单个学生信息>
# 2. 方便遍历所有学生  数据容器的嵌套 列表 [{学生1}, {学生2}, {学生3}]
    # ( {学生1}, {学生2}, {学生3} )  元组是一种不可变的数据容器
students = [
    {'name': name, 'chinese': chinese, 'math': math, 'english': english, 'total': total, }
]

print(students)
