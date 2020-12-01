import requests
import lxml
from bs4 import BeautifulSoup
from pprint import pprint
url='http://quotes.toscrape.com/tag/'
type_=["love","inspirational","life","humor","books","reading","friendship","friends","truth","simile",]
for i in range(len(type_)):
    r=requests.get(url+type_[i])
    print(url+type_[i])
    soup=BeautifulSoup(r.text,'lxml')
    # pprint(soup)
    quotes=soup.find_all('span',class_='text')
    # print(quotes)
    author=soup.find_all('small',class_='author')
    tags=soup.find_all('div',class_='tags')
    # print(tags)
    with open('Allquotes.txt','a',encoding='utf-8') as f:
        f.write('\n\n')
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