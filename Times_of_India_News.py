import requests
import lxml
from bs4 import BeautifulSoup

url='https://timesofindia.indiatimes.com/briefs'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
outlets=soup.find_all('div',class_='brief_box')
# print(outlets)
with open('TimesofIndiaBrief.txt','w') as f:
    for i in outlets:
        try:
            h2=i.find('h2')
            p=i.find('p')
            if p is not None:
                a=p.find('a')
            href=h2.find('a')
        except:
            pass
        else:
            print(f'{"Title".ljust(8)} : {h2.text}')
            print(f'{"View".ljust(8)} : https://timesofindia.indiatimes.com{href.get("href")}')
            print(f'{"Breif".ljust(8)} : {a.text}')
            f.write(f'{"Title".ljust(8)} : {h2.text}\n')
            f.write(f'{"View".ljust(8)} : https://timesofindia.indiatimes.com{href.get("href")}\n')
            f.write(f'{"Breif".ljust(8)} : {a.text}\n')
            f.write('\n')

        print()