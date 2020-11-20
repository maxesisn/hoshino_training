import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from hoshino.modules.hoshino_training.util.module import *

URL_CN = 'https://bbs.nga.cn/thread.php?stid=20775069'

async def new_get_nga_cookies():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(URL_CN)
    await asyncio.sleep(5)
    cookies = driver.get_cookies()
    driver.quit()
    cookies_dict = {}
    for cookie in cookies:
        cookies_dict[cookie['name']] = cookie['value']
    return cookies_dict

module_replace('hoshino.modules.GWYOG-Hoshino-plugins.ngaclanbattlespider','get_nga_cookies',new_get_nga_cookies)