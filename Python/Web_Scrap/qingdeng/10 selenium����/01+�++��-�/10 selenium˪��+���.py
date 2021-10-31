from selenium import webdriver

# 创建浏览器对象的时候添加配置
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 配置浏览器的某个属性
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
    })
"""
})

driver.get('http://epub.cnipa.gov.cn/index.action')

print(driver.page_source)

input()
driver.quit()

"""
    检测selenium不是所有的检测都是这样的
    js检测,  解密
"""
