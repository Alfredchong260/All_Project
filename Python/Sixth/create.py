import os

file_name = 'Lesson'

for i in range(1, 10):
    file = open(file_name + str(i) + '.py', 'w')
    file.close()

