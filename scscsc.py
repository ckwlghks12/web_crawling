from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
import re
import requests
import time


csv_filename_to_write = "unpareview.csv"
csv_open = open(csv_filename_to_write, 'w+',encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('title', 'image_url'))

# url1 = "https://www.unpa.me/review/detail/b1a8a3b2-f700-4448-a4f2-0e3655481135"
url1 = 'https://www.unpa.me/review/detail/4378c70c-a922-40be-a686-4dfdfbac1329'

driver = webdriver.Chrome('/Users/ji/chromedriver')
driver.get(url1)
driver.implicitly_wait(3)
html = driver.page_source
bs = BeautifulSoup(html,'html.parser')

# comment = driver.find_elements_by_class_name('content')


comment = driver.find_element_by_class_name('unpa-comments')
commentt = comment.find_elements_by_class_name('content')

for i in commentt:
    print(i.find_element_by_class_name('user-name').text)
    print(i.find_element_by_class_name('time').text)
    print(i.find_element_by_class_name('count').text)
    print(i.find_element_by_class_name('text').text)
    try:
        print(i.find_element_by_class_name('emoticon').find_element_by_tag_name('img').get_attribute('src'))
    except :
        continue
# comuser = comment.find_elements_by_class_name('user-name')
# comtime = comment.find_elements_by_class_name('time')
# comlike = comment.find_elements_by_class_name('count')
# combody = comment.find_elements_by_class_name('text')

# for i in comuser:
#     print(i.text)
# for i in comtime:
#     print(i.text)
# for i in comlike:
#     print(i.text)
# for i in combody:
#     print(i.text)


# if int(driver.find_element_by_class_name('comment-count-title-count').text) > 0:
#     commen = driver.find_elements_by_class_name('unpa-comments')
#     pic = driver.find_element_by_class_name('unpa-comments')
#     commentpic = pic.find_elements_by_class_name('user-profile-image')
#     for i in commen:
#         print(i.text.split('\n'))
#     for i in commentpic:
#         print(i.get_attribute('style'))
        

# driver.close()

