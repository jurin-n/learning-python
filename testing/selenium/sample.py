# -*- coding: utf-8 -*-

from selenium import webdriver
import sys

path_to_driver = sys.argv[1] # Chrome Driverへの絶対パス
path_to_screenshot = sys.argv[2] # スクリーンショット格納場所の絶対パス

# driver = webdriver.Firefox()
# Optional argument, if not specified will search path.
# driver = webdriver.Chrome('/path/to/chromedriver')
driver = webdriver.Chrome(path_to_driver)

driver.get('http://example.selenium.jp/reserveApp')
driver.find_element_by_id('guestname').send_keys(u'サンプルユーザ')
driver.get_screenshot_as_file(path_to_screenshot + '/foo.png')
driver.find_element_by_id('goto_next').click()
driver.quit()
