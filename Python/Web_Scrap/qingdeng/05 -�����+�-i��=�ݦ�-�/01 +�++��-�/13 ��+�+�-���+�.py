import re

email_list = ['xiaowang@163.com', 'xiaowang@163.comheihei', '.com.xiaowang@qq.com']

"""
^   限制开头
$   限制结尾
"""
for email in email_list:
    result = re.findall('^\w+@163\.com$', email)
    if result:
        print(f' {email} 是规范的邮件地址, 地址是 {result[0]}')
    else:
        print(f' {email} 不是规范的邮件地址')
