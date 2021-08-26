"""
思路：
    将照片转换成黑白
    将像素转换成字符
"""
from PIL import Image

char_list = '''@B%8&WM#*oahkbdpqwmZO0QLCJUVYXzcvunxrjft/\|()1{}[]?-_+~<>i!1I;:,"^``.'''
count = len(char_list)

# 将彩色转换成黑白
def transfer(image_file):
    image_file = image_file.convert("L")
    image_file.show()
    codePic = ''

    for h in range(0, image_file.size[1]): # 纵1 横0
        for w in range(0, image_file.size[0]):
            gray = image_file.getpixel((w, h))
            # print(gray)
            codePic = codePic + char_list[int((count * gray) / 256)]
        codePic = codePic + '\n'

    return codePic

image_file = Image.open("./amon.jpg")
text = transfer(image_file)
print(text)
tmp = open(r"./output.txt", "w")
tmp.write(text)
tmp.close()
