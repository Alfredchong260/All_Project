import os  # 文件目录操作的模块  内置模块


"""创建文件夹"""
# os.mkdir('python')  # 创建文件夹, 括号内部填写文件的路径(绝对路径/相对路径)
                    # 当文件已存在时，无法创建该文件, 会报错

"""重命名文件"""
# os.rename('需要修改名字的文件夹/文件', '新名字')
# os.rename('python', 'python110')  # 重命名文件夹/文件

"""删除文件夹"""
# os.rmdir('python110')  # 删除文件夹, 只能删除空文件夹, 没有此文件夹会报错

"""删除文件"""
# os.remove('hello.txt')

"""获取当前目录文件"""
# result = os.listdir('python')  # 获取当前文件夹下面所有的文件, 返回一个列表, 括号内部指定的是文件夹的路径
# print(result)


"""判断文件/文件夹是否存在"""
# result = os.path.exists('python')  # 如果文件路径存在返回True, 不存在返回 False
# print(result)

if not os.path.exists('python'):  # 如果 python 是不存在的
    os.mkdir('python')

