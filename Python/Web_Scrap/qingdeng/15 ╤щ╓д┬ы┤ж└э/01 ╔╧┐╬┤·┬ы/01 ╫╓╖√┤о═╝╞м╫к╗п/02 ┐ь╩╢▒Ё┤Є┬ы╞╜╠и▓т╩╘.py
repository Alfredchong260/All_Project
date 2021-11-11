import base64
import requests
from constants import KUAI_USERNAME, KUAI_PASSWORD


def base64_api(img):
    """
    定义识别验证码的函数
    :param uname: 快识别网站的用户名
    :param pwd: 快识别网站的密码
    :param img: 传入的图片路径
    :param typeid: 识别验证码的类型
    :return:
    """
    with open(img, 'rb') as f:  # 根据传入的图片路径打开图片文件
        base64_data = base64.b64encode(f.read())  # 把二进制形式的图片编码
        b64 = base64_data.decode()  # 返回图片的字符串形式

    data = {"username": KUAI_USERNAME, "password": KUAI_PASSWORD, "typeid": 1003, "image": b64}  # 提交的表单数据


    result = requests.post("http://api.ttshitu.com/predict", json=data).json()
    print(result)

    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


if __name__ == "__main__":
    img_path = "yzm.png"
    result = base64_api(img=img_path)
    print(result)
