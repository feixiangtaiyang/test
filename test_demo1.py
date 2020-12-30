from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无界面
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
#driver = webdriver.Chrome()123

driver.get("https://www.baidu.com/")
