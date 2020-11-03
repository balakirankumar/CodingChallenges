import requests
import lxml
from bs4 import BeautifulSoup
from pprint import pprint
url='https://www.flipkart.com/search?q=apple+ipad&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_3_6_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_3_6_na_na_na&as-pos=3&as-type=HISTORY&suggestionId=apple+ipad&requestId=72f37bad-bccb-4f46-9f44-c610bc925da8&as-backfill=on'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
product=soup.find_all('div',class_='_3liAhj')
name=soup.find_all('a',class_='_2cLu-l')
presentprice=soup.find_all('div',class_='_1uv9Cb')
pastprice=soup.find_all('div',class_='_3auQ3N')
z=1
with open('Apples1.txt','w') as f:
    for i in product:
        name=i.find('a',class_='_2cLu-l').text
        presentprice=i.find('div',class_='_1vC4OE').text
        try:
            pastprice=i.find('div',class_='_3auQ3N').text
        except:
            pastprice="None"
        try:
            offer=i.find('div',class_='VGWI6T').text
        except:
            offer="None"
        rating=i.find('div',class_='hGSR34').text
        Details=f'Product No : {z}\nProduct : {name}\nPresentPrice : {presentprice[1:]} INR\nPastPrice : {pastprice[1:]} INR\nRating : {rating}\nOffer : {offer}'
        f.write(Details)
        f.write('\n\n')
        print(Details)
        print()
        z+=1
pages=soup.find('nav',class_='_1ypTlJ')

urls=[]
links=pages.find_all('a',class_='_2Xp0TH')
for i in links:
    pagenum=int(i.text) if i.text.isdigit() else None
    if pagenum != None :
        href=i.get('href')
        urls.append(href)
urls=urls[1:]
with open('Apples1.txt','a') as f:
    for i in urls:
        r=requests.get(url)
        soup=BeautifulSoup(r.text,'lxml')
        product=soup.find_all('div',class_='_3liAhj')
        name=soup.find_all('a',class_='_2cLu-l')
        presentprice=soup.find_all('div',class_='_1uv9Cb')
        pastprice=soup.find_all('div',class_='_3auQ3N')
        for i in product:
            name=i.find('a',class_='_2cLu-l').text
            presentprice=i.find('div',class_='_1vC4OE').text
            try:
                pastprice=i.find('div',class_='_3auQ3N').text
            except:
                pastprice="None"
            try:
                offer=i.find('div',class_='VGWI6T').text
            except:
                offer="None"
            rating=i.find('div',class_='hGSR34').text
            Details=f'Product No : {z}\nProduct : {name}\nPresentPrice : {presentprice[1:]} INR\nPastPrice : {pastprice[1:]} INR\nRating : {rating}\nOffer : {offer}'
            f.write(Details)
            f.write('\n\n')
            print(Details)
            print()
            z+=1


