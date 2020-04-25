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
csv_writer.writerow( ('top_img','brand','productname','rating','body','like_count','upload_at','views','comment','comment_picture',"파워리뷰","com_count","com_date","comment_rating","urlss","ruser","rusername","ruserskin_type","ruserskin_tone","rucount"))

url1 = "https://www.unpa.me/review"
# url1 = "https://www.unpa.me/review/detail/76180522-9d10-4584-8762-9e68d2e47d7d"

driver = webdriver.Chrome('/Users/ji/chromedriver')
driver.get(url1)
driver.implicitly_wait(3)
html = driver.page_source
bs = BeautifulSoup(html,'html.parser')

for i in range(0,0):
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
    
    top_img = bs.find('div',class_='product-image') 
    topimg_url = top_img.attrs['style']
    
    if topimg_url.find('default') == -1 :
        topimg = topimg_url[topimg_url.index('http'):topimg_url.rindex('\'')]
    else :
        topimg = "default"
        # print("topimg=",end=""), print(topimg)
        
    review_title = bs.findAll('div',{'class':re.compile("product-info-box")})
    body = bs.find('div',{'class':re.compile("body")})
    like_count = bs.find('div',class_='count')
    bot_time = bs.find('span', class_='time')
    bot_view = bs.find('span', class_='view')


    brand = (review_title[0].find('div',class_='brand-name').text)
    productname = (review_title[0].find('div',class_='product-name').text)
    rating = review_title[0].find('span',class_='rating-value').text.strip()
    bodycon = body.find('div',class_='content')
    like_count = like_count.text
    btime = bot_time.text
    bview = bot_view.text # 여기까지 본문 밑에 조회수까지
    
    # # 여기서부터 작성자 다른 파워리뷰
    commen = driver.find_elements_by_class_name("other-feeds")
    other = driver.find_element_by_class_name('other-feeds')
    count = other.find_elements_by_class_name('horizontal-count-info')
    compro = bs.findAll('div',class_="user-profile-image")
    
    if int(driver.find_element_by_class_name('comment-count-title-count').text) > 0:
        comment = driver.find_elements_by_class_name('unpa-comments')
        pic = driver.find_element_by_class_name('unpa-comments')
        commentpic = pic.find_elements_by_class_name('user-profile-image')
        for i in comment:
            com = i.text.split('\n')
        for i in commentpic:
            compic = i.get_attribute('style')
        # for i in com:
        #     if i == '답글달기':
        #         del com[i]
    else :
        com = []
        compic = []
    
    comra = []
    urlss = []
    combody = []
    counts = []     
    redate = []
    if len(commen) > 0:
        otherfeed = bs.find('div',class_= "other-feeds").findAll('div',class_='image')
        for i in commen: 
            bowl = i.find_elements_by_class_name('body')
            comenrating = i.find_elements_by_class_name('rating-value')
        for i in bowl:
            combody.append(i.text.split('\n'))
        for i in comenrating:
            comra.append(i.text)
        for i in otherfeed: # 밑 파워리뷰 썸네일
            url = i.attrs['style']
            urlss.append(url[url.index('http'):url.rindex('\'')])

        for i in count:
            redate.append(i.find_element_by_class_name('pull-right').text)
            for e in i.find_elements_by_class_name('count'):
                counts.append(e.text)
            
    uprourl = bs.find('div',class_='user-image').get('style') # 오른쪽 유저 프로필사진
    if uprourl.find('default') == -1 :
        ruser = uprourl[uprourl.index('http'):uprourl.rindex('\'')] # 오른쪽 유저 프로필사진
            

    userskin = bs.find('div',class_='user-skin-info').findAll('div') # 오른쪽 유저 피부정보
    usercount = bs.find('div',class_="user-count-info").findAll('div') # 오른쪽 유저 팔로워 등등 숫자
    
    uca = []
    
    for i in usercount:
        uca.append(i.text)
    
    rusername = bs.find('div',class_='user-nickname').text.strip() # 오른쪽상단 유저이름
    ruserskin_type = userskin[0].text
    ruserskin_tone = userskin[1].text # 유저피부타입
    
    rucount = []
    
    for i in usercount: # 오른쪽 유저 카운트
        rucount.append(i.text)
        
    time.sleep(2)
    csv_writer.writerow ((topimg,brand,productname,rating,bodycon,like_count,btime,bview,com,compic,combody,counts,redate,comra,urlss,ruser,rusername,ruserskin_type,ruserskin_tone,rucount))
        
        
csv_open.close()
driver.close()