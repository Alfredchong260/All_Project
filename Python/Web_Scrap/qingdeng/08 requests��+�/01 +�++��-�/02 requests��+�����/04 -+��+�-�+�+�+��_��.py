import requests
proxy_response = requests.get('http://106.52.167.142')
print(proxy_response.status_code)


"""
requests.exceptions.ConnectionError   连接错误

目标服务器数据没有: ip被封, 案例, 
客户端的问题: 网络的连通性不好
服务器问题: 服务器瘫痪
"""