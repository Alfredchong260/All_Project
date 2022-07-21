import os

source = '/home/cms/.Project/Python/own/scrap/leshe/'

for i in os.listdir(source):
    if not (i.endswith('jpg') or i.endswith('png')) and not i.endswith('py'):
        os.chdir(source + i)
        for j in os.listdir():
            os.rename(source + i + '/' + j, source + j)

for i in os.listdir(source):
    if not (i.endswith('jpg') or i.endswith('png')) and not i.endswith('py'):
        os.rmdir(source + i)

