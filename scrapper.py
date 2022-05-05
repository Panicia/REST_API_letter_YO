from bs4 import BeautifulSoup
import requests
import re
import os

class Yo():
    def __init__(self):
        self._words = []
        self.loadData()

    def loadData(self):
        if not os.path.exists('tryYO2.txt'):
            self.__page_link = 'http://www.yomaker.ru/yoslovar.htm'
            page_response = requests.get(self.__page_link, timeout=5)
            page_content = BeautifulSoup(page_response.content, "html.parser")
            texts = page_content.find_all('p')

            w = open('tryYO1.txt', 'w', encoding = 'utf-8')
            for t in texts:
                w.write(t.text + '\n')
            w.close()

            r = open('tryYO1.txt', 'r', encoding = 'utf-8')
            i = 0
            for word in r:
                i += 1
                if i > 45 and re.fullmatch(r'[а-я]|ё', word[0]):
                    m = re.split(r'\[|\]|,|\(|\)|\n|;|»|«| |:|’|-|\"', word)
                    for w1 in m:
                        if w1.find('ё') != -1:
                            self._words.append(w1.strip().lower())
            r.close()
            self._words = list(set(self._words))
            self._words.sort()

            with open('tryYO2.txt', 'w', encoding = 'utf-8') as f:
                for i in self._words:
                    f.write(i + '\n')
        else:
            with open('tryYO2.txt', 'r', encoding = 'utf-8') as f:
                for line in f:
                    self._words.append(line.strip())

    def getWords(self):
        return self._words

    def getValid(self, word):
        return word in self._words
