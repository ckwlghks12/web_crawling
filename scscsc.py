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
url1 = 'https://www.unpa.me/review/detail/445fc234-f08a-492b-8d83-d986a1fd39e0'

driver = webdriver.Chrome('/Users/ji/chromedriver')
driver.get(url1)
driver.implicitly_wait(3)
html = driver.page_source
bs = BeautifulSoup(html,'html.parser')

other = driver.find_element_by_class_name('other-feeds')
count = other.find_elements_by_class_name('horizontal-count-info')

carr = []
redate = []
for i in count:
    redate.append(i.find_element_by_class_name('pull-right').text)
    for e in i.find_elements_by_class_name('count'):
        carr.append(e.text)

print(carr,redate)

# if int(driver.find_element_by_class_name('comment-count-title-count').text) > 0:
#     commen = driver.find_elements_by_class_name('unpa-comments')
#     pic = driver.find_element_by_class_name('unpa-comments')
#     commentpic = pic.find_elements_by_class_name('user-profile-image')
#     for i in commen:
#         print(i.text.split('\n'))
#     for i in commentpic:
#         print(i.get_attribute('style'))
        

driver.close()

