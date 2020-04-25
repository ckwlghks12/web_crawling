from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import csv
import re
import requests
import time

csv_filename_to_write = "unpareview.csv"
csv_open = open(csv_filename_to_write, 'w+',encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow( ('title', 'image_url'))

url1 = "https://www.unpa.me/review"
# url = "https://www.unpa.me/review/detail/b7692e83-4b9a-4797-89c7-1f9a3316c185"


driver = webdriver.Chrome('/Users/ji/chromedriver')

driver.get(url1)



driver.implicitly_wait(3)



html = driver.page_source
bs = BeautifulSoup(html,'html.parser')
for i in range(0,2):
    driver.find_element_by_class_name('unpa-load-more-button').click()   # 더보기 클릭
    time.sleep(1)


products = driver.find_elements_by_class_name('unpa-card')
product_ids = []
for product in products:
    if len(product.get_attribute('id')) > 0 :
        product_ids.append(product.get_attribute('id'))      # 아이디 추출

print(product_ids)



for product_id in product_ids:
    ID = product_id
    url = f'https://www.unpa.me/review/detail/{ID}'
    driver.get(url)
    html = driver.page_source
    bs = BeautifulSoup(html,'html.parser')
    
    # commen = driver.find_elements_by_class_name("other-feeds")
    # count = driver.find_elements_by_class_name('horizontal-count-info')
    # compro = bs.findAll('div',class_="user-profile-image")
    # top_img = bs.find('div',class_='product-image')
    # topimg_url = top_img.attrs['style']
    # review_title = bs.findAll('div',{'class':re.compile("product-info-box")})
    # body = bs.find('div',{'class':re.compile("body")})
    # like_count = bs.find('div',class_='count')
    # bot_time = bs.find('span', class_='time')
    # bot_view = bs.find('span', class_='view')
    # if int(bs.find('span',class_='comment-count-title-count').text) > 0:
    #     print(int(bs.find('span',class_='comment-count-title-count').text) > 0)
    #     com = bs.findAll('.comment-content')
    #     username = com[0].select('.user-name')
    #     ment = com[0].findAll('div',class_='text')
    #     comcon = bs.select(".comment-content")
    #     uname = bs.select(".user-name")[0]
    #     for i in ment :
    #         print(i.text)
    #     for i in username:
    #         print(i.find('div').text)


    userskin = bs.find('div',class_='user-skin-info').findAll('div')
    usercount = bs.find('div',class_="user-count-info").findAll('div')
    otherfeed = bs.find('div',class_= "other-feeds").findAll('div',class_='image')
    
    
    # print(topimg_url[topimg_url.index('http'):topimg_url.rindex('\'')])
    # print(review_title[0].find('div',class_='brand-name').text)
    # print(review_title[0].find('div',class_='product-name').text)
    # print(review_title[0].find('span',class_='rating-value').text.strip())
    # print(body.find('div',class_='content'))
    # print(like_count.text)
    # print(bot_time.text,bot_view.text)




    # for e in comcon:
    #     print(e.findAll('a',class_='user-name')[0].find('div').text)
    #     print(e.findAll('span')[0].text,e.findAll('span')[1].text)
    
    # for i in compro:
    #     ur = i.attrs['style']
    #     print(ur[ur.index('http'):ur.rindex('\'')])

    print(bs.find('div',class_='user-nickname').text.strip()) # 오른쪽상단 유저이름

    print(userskin[0].text,userskin[1].text) # 유저피부타입
    for i in usercount:
        print(i.text)


    for i in otherfeed: # 밑 파워리뷰 썸네일
        url = i.attrs['style']
        print(url[url.index('http'):url.rindex('\'')])

    # for i in commen: 
    #     bowl = i.find_elements_by_class_name('body')
    #     comenrating = i.find_elements_by_class_name('rating-value')

    # for i in bowl:
    #     print(i.text)
    # for i in count:
    #     print(i.text)

    # for i in comenrating:
    #     print(i.text)
        

    # brand = driver.find_element_by_class_name('unpa-tip-detail-header').text
    # description = driver.find_element_by_class_name('resources').text
    # like_number = driver.find_element_by_class_name('count').text
    # review = driver.find_element_by_class_name('comment-count-title-count').text
    time.sleep(2)







# driver.find_element_by_class_name('review-contents').click()


driver.close()