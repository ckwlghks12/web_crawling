from bs4 import BeautifulSoup
import csv
import re
import requests

crawling_url = 'http://wwww.vogue.co.kr/category/fashion/'

csv_filename_to_write = "fashion_all.csv"
csv_open = open(csv_filename_to_write, 'w+',encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('title', 'image_url'))




req = requests.get(crawling_url)

html = req.text
#print("html=",end=""),print(html)

bs = BeautifulSoup(html, 'html.parser')

article_list = bs.findAll('article', {'id' : re.compile('post-*')})

#print("article_list=",ends=""), print(article_list)

for article in article_list:
    h2_title = article.findAll('h2')
    #print("h2_titles=",end=""),print(h2_title)
    title = h2__title[0].text
    #print("title=",end=""),print(title)

    img= article.find('img')
    image_url = img('src')
   # print("image_url=",end=""),print(image_url)

    csv_writer.writerow ( ( title, image_url))


csv_open.close()
