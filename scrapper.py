from bs4 import BeautifulSoup
import requests
import re

page_link = 'http://www.yomaker.ru/yoslovar.htm'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
texts = page_content.find_all('p')

w = open('tryYO1.txt', 'w', encoding = 'utf-8')
for t in texts:
    w.write(t.text + '\n')
w.close()

r = open('tryYO1.txt', 'r', encoding = 'utf-8')
fileWords = open('tryYO2.txt', 'w', encoding = 'utf-8')
words = []
i = 0
for word in r:
    i += 1
    if i > 45 and re.fullmatch(r'[а-я]', word[0]):
        m = re.split(r'\[|,|\(|\)|\n|;| |-', word)
        for w1 in m:
            if w1.find('ё') != -1 and w1 != 'ён':
                words.append(w1 + '\n')
                fileWords.write(w1 + '\n')
r.close()
fileWords.close()
