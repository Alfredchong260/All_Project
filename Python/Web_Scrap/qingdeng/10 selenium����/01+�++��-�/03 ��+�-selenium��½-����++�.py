"""
京东数据采集
"""
import csv
import time
from selenium.webdriver.chrome.options import Options  # 浏览器的可选项
from selenium import webdriver


def get_product(keyword):
    """实现商品搜索功能"""
    driver.find_element_by_css_selector('#key').send_keys(keyword)
    # 点击搜索
    driver.find_element_by_css_selector('.button').click()

def drop_down():
    """模拟页面下拉操作"""
    for h in range(1, 11, 2):  # 13579  控制页面滚动的次数 页面高度会变化
        j = h / 10   # 1/10  3/10  5/10  7/10  9/10
        js = "document.documentElement.scrollTop=document.documentElement.scrollHeight*%f" % j
        driver.execute_script(js)
        time.sleep(0.5)

def parse_data():
    """解析数据, 保存"""
    lis = driver.find_elements_by_css_selector('.gl-item')  # li标签

    for li in lis:
        name = li.find_element_by_css_selector('div.p-name a em').text  # 商品名字
        name = name.replace('京品电脑', '').replace('京东超市', '').replace('\n', '').replace('京品文具', '')

        price = li.find_element_by_css_selector('div.p-price strong i').text  # 价格
        deals = li.find_element_by_css_selector('div.p-commit strong a').text  # 评论数量
        shop_name = li.find_element_by_css_selector('span.J_im_icon a').text  # 店铺名字
        print(name, price, deals, shop_name, sep=' | ')

        with open('京东数据.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([name, price, deals, shop_name])

def get_next():
    """下一页点击"""
    driver.find_element_by_css_selector('.pn-next').click()


word = input('请输入商品搜索关键字:')

chrome_options = Options()  # 实例化对象
chrome_options.add_argument('--headless')  # 添加一个可选项  # --headless 指代无头模式
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
driver.get('https://www.jd.com/')
# driver.maximize_window()
driver.implicitly_wait(10)

# 调用商品搜索的函数
get_product(word)

for page in range(100):
    # 调用页面下拉的函数
    drop_down()
    # 调用商品解析函数
    parse_data()
    # 调用点击下一页函数
    get_next()

input()
driver.quit()



