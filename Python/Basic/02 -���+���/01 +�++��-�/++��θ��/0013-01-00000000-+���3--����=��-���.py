"""
需求：构建笔趣阁所有类别的前10页的url地址
分析:
    玄幻前10页网址
        http://www.shuquge.com/category/1_1.html
        http://www.shuquge.com/category/1_2.html
        http://www.shuquge.com/category/1_3.html
        ......
        http://www.shuquge.com/category/1_10.html
    武侠前10页网址
        http://www.shuquge.com/category/2_1.html
        http://www.shuquge.com/category/2_2.html
        http://www.shuquge.com/category/2_3.html
        ......
        http://www.shuquge.com/category/2_10.html

分析上面网页地址可以得出结论。页面是通过 1_1.html 的形式来确定的
下划线前面部分是类别，后面部分是页面。
玄幻：1
武侠: 2
都市：3
历史：4
侦探：5
网游：6
科幻：7

小提示：如果不会自己写循环，可以复制下面代码运行一下
for cate in range(0, 8):
    for page in range(0, 11):
        print(f'cate:{cate}_page:{page}')
"""
"""请在下方编写代码"""
for cate in range(1, 8):
    for page in range(1, 11):
        # print(f'cate:{cate}_page:{page}')
        print(f'http://www.shuquge.com/category/{cate}_{page}.html')
