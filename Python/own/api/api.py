import requests
import time
import re
se = requests.session()
 
if __name__ == '__main__':
    Post_url = "http://api-ok.xiaofamao.com/api.php?json=0&v=1&key=xxxxxx" #自己想办法弄到key
    Post_data = {
        'wenzhang': '床前明月光，疑是地上霜。'
    }
    Text = se.post(Post_url, data=Post_data).text.replace("'", '"').replace('/ ', '/')
    print(Text)
