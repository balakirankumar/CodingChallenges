import requests
import lxml
from bs4 import BeautifulSoup
from pprint import pprint

url=['https://www.v6velugu.com/telangana-breaking-news/','https://www.v6velugu.com/Hyderabad-breaking-news/']
for i in url:
    r=requests.get(i)
    soup=BeautifulSoup(r.text,'lxml')
    li=soup.find_all('li',class_='listing-item')
    # print(li)
    print()
    for i in li:
        print(i.text)
        a=i.find('a','title')
        print(a.get('href'))
        print()
    print('\n\n\n\n')