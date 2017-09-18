# -*- coding: utf-8 -*-

from selenium import webdriver
import sys
import os

driver_name = sys.argv[1] # Driver選択用

# driver = webdriver.Firefox()
# Optional argument, if not specified will search path.
# driver = webdriver.Chrome('/path/to/chromedriver')
if driver_name =='Firefox':
    print('seleted Firefox Driver.')
    driver = webdriver.Firefox()
elif driver_name =='Chrome':
    print('seleted Chrome Driver.')
    driver = webdriver.Chrome()
else:
    raise Exception()

dir_for_screenshot = os.path.join(os.getcwd(), 'screen-shot')
dir_for_html_source = os.path.join(os.getcwd(), 'html-source')

if not os.path.exists(dir_for_screenshot):
    os.makedirs(dir_for_screenshot)

if not os.path.exists(dir_for_html_source):
    os.makedirs(dir_for_html_source)


screenshot_file = os.path.join(dir_for_screenshot, 'foo'+ '_'+ driver_name +'.png')
html_source_file = os.path.join(dir_for_html_source, 'foo'+ '_'+ driver_name +'.html')

driver.get('http://example.selenium.jp/reserveApp_Renewal/')
driver.find_element_by_id('guestname').send_keys(u'サンプルユーザ')
driver.save_screenshot(screenshot_file)

page_source_file = open(html_source_file,'wb')
page_source_file.write(driver.page_source.encode())
page_source_file.close()

driver.find_element_by_id('agree_and_goto_next').click()
driver.quit()
