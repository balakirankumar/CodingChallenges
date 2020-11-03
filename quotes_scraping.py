import requests
import lxml
from bs4 import BeautifulSoup
from pprint import pprint
url='http://quotes.toscrape.com/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
# pprint(soup)
quotes=soup.find_all('span',class_='text')
# print(quotes)
author=soup.find_all('small',class_='author')
tags=soup.find_all('div',class_='tags')
# print(tags)
with open('quotes.txt','w') as f:
    for i in range(len(quotes)):
        print(author[i].text)
        print(quotes[i].text)
        f.write(f"Said by {author[i].text} \n")
        f.write(quotes[i].text+'\n')
        f.write('Tags : ')
        tag=tags[i].find_all('a',class_='tag')
        print('Tags : ',end=' ')
        for j in tag:
            print(j.text,end=' ')
            f.write(j.text)
            f.write('  ')
        print('\n')
        f.write('\n\n\n')