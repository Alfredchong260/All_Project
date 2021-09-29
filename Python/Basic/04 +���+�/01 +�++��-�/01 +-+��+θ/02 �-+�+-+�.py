# r : 打开一个文件, 以只读的方式打开, 如果找不到文件会报错
file = open('hello.txt', mode='r', encoding='utf-8')

text = file.read()

file.close()

print(text)
