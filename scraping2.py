from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

import requests

crawling_url = "http://www.vogue.co.kr/category/fashion/page/1"

html_doc = urlopen(crawling_url)

bs = BeautifulSoup(html_doc.read(), 'html.parser')

post_select = bs.select()
print("post_select=",end=""), print(post_selected[0].text)
