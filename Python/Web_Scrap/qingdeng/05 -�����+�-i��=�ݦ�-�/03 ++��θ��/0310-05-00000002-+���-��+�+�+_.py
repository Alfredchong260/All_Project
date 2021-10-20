
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
"""

tel = "18123115458"

import re

def change(tel):
    tel = str(tel)
    length = len(tel)
    if length >= 11:
        front = tel[0:3]
        middle = tel[3:6]
        back = tel[-4:-1]
        changed = re.sub(middle, '*'*len(middle), middle)
        return front + changed + back
    else:
        front = tel[0:3]
        middle = tel[3:]
        changed = re.sub(middle, '***', middle)
        return front + changed


new = change(tel)
print(new)
