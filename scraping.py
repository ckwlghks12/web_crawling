from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import csv
import re
import requests
import time

crawling_url = 'https://www.unpa.me/review/detail/e077b4da-2575-4b6f-bdc2-4ca0d458bfd1'

csv_filename_to_write = "unpareview.csv"
csv_open = open(csv_filename_to_write, 'w+',encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('title', 'image_url'))

driver = webdriver.Chrome('/Users/ji/chromedriver')


req = requests.get(crawling_url)

html = req.text
# print("html=",end=""),print(html)

bs = BeautifulSoup(html, 'html.parser')

driver.get("https://www.unpa.me/review/detail/e077b4da-2575-4b6f-bdc2-4ca0d458bfd1")
driver.implicitly_wait(3)

geto = driver.find_elements_by_class_name('comment-content')
for i in geto:
    print(i.text)
    

top_img = bs.find('div',class_='product-image')
topimg_url = top_img.attrs['style']
review_title = bs.findAll('div',{'class':re.compile("product-info-box")})
body = bs.find('div',{'class':re.compile("body")})
like_count = bs.find('div',class_='count')
bot_time = bs.find('span', class_='time')
bot_view = bs.find('span', class_='view')
# comment = bs.find('div',class_='load-more-comments')
# userprofile = bs.findAll('div',class_= "text")

# selected= bs.select('div > div.col-sm-9.col-sm-pull-3.left > div.footer > div.unpa-comments.loadable > div:nth-child(2) > div.content > div.text')
# print("selected=",end=""), print(selected)



print(topimg_url[topimg_url.index('http'):topimg_url.rindex('\'')])
print(review_title[0].find('div',class_='brand-name').text)
print(review_title[0].find('div',class_='product-name').text)
print(review_title[0].find('span',class_='rating-value').text.strip())
print(body.find('div',class_='content'))
print(like_count.text)
print(bot_time.text,bot_view.text)
# print(comment)
# print(userprofile)

# for i in body[0].findAll('img'):
#     print(i.get('src'))
# print("article_list=",ends=""), print(article_list)

for article in article_list:
  
    h2_title = article.findAll('h2')
    #print("h2_titles=",end=""),print(h2_title)
    title = h2_title[0].text
    #print("title=",end=""),print(title)
    img= article.find('img')
    image_url = img['src']
   # print("image_url=",end=""),print(image_url)   
    csv_writer.writerow ((title, image_url))


csv_open.close()
driver.close()