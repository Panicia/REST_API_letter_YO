from bs4 import BeautifulSoup
import requests
page_link = 'http://www.yomaker.ru/yoslovar.htm'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
texts = page_content.find_all('p')
w = open('try1.txt', 'w')
for t in texts:
    w.write(t)
