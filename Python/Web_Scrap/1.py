'''
install request
爬虫配合数据分析可以实现很多东西
'''

'''
URI 和 URL

    URI 统一资源标识符
        例：

    URL 统一资源定位符
        例：https://www.google.com
        就算url中有参数依旧是url,本质上一样的

    超文本(hypertext)
        浏览器看到的网页都由超文本解析而成的
        浏览器通过解析网页源代码来呈现相关网页
        网页源代码就是使用超文本来编写的

    <body>需要爬取的数据</body>
    <body></body> 就是标签
    <div></div>   块标签 它是一块块的 每一块都有不同的元素
    <a></a>       放跳转链接 href
    <img>         添加图片的
    <p>           段落 paragraph

HTTP 和 HTTPS
    http是必须有的
    这是访问资源需要的协议

    两种协议
    http: 超文本传世协议, http协议用来网络传输超文本数据
    https 是一个协议

    http协议用于网络传输超文本数据，到本地浏览器的协议
    http是一个开发团队做的，目前使用版本为http1.1的版本

    https中的 s=SSL
    https是以安全为目的的http协议，多了SSL
    SSl是一个加密的方式,可对传输的数据进行加密
    https也是看为安全版的http

    如果访问是网址是http的网页，就会弹出一个弹窗显示不安全

    (chrome) name: 请求的名称
    (firefox) domain: 请求的名称

    status: 响应的状态码
        200为正常的响应
        404为错误的响应

    type为文档类型 
        document: html的代码

    initator: 请求源，用于标记这个对象或者这个进程是由这个对象发起的

    size: 服务器返回的文件和资源的大小

    time: 发起请求到获取响应的总时间

'''

'''
    请求
        请求是客服端向服务器发出的
            可以分为
                请求方法: (Request Method)
                    - GET
                        一般在浏览器输入的网址就是发起一个GET的请求,请求的参数在url中
                        一个网址，有些参数不重要，有些很重要
                        每个参数以&作为分割
                    - POST
                        用于提交数据，通常用来做帐号和密码登陆的操作
                        进行了表单的提交，参数在请求体中
                    - PUT
                    - DELETE
                    - OPTIONS
                    - CONNECT
                    - TEACE

                    get 请求的数据通常只有1024字节
                    post是没有大小限制

                请求头  : (Request headers)
                    用来说明服务器使用的附加条件
                        - Cookies
                        - Referer
                        - User-Agent

                        Accept: 请求报头域，由于指定客服短可以接受哪些类型的信息
                        Accept-Language: 可接受的语言
                        Host: 请求资源的主机ip和端口号，用于请求url原始服务器位置
                        Cookie: 储存对方服务器存放在本地的数据,保存信息作为标识
                        Referer: 用来标识这个请求是哪个页面发过来的
                        User-Agent: 现实客服端的信息
                        伪装电脑的信息，让对方服务器不认为是爬虫

                请求体  : (Request body)
                    用来存储post提交的数据
                    post请求表单数据
                    form data

                请求的网址: (Request URL)
        
        有些网站，密码是直接显示出来的
        还有一些网站密码和帐号是经过加密处理的

    解码的操作
        80-90%的网站的密码都是直接现实出来的

        响应
            是由服务器返回给客服端的
            可以分为三个部分
                响应的状态码
                    比如200
                响应头
                    date 标识响应产生的时间
                    server: 包含了服务器的信息，比如名称和版本
                    set-cookie: 设置cookies高数浏览器需要将此内容放在cookies中
                    content-type: 文档类型
                    
                响应体
                    正文的数据都在响应体中的HTML代码，需要爬取的数据
'''
