import requests
import lxml
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np
import pandas as pd

url='https://www.cricbuzz.com/cricket-series/3130/indian-premier-league-2020/points-table'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
table=soup.findAll('table',class_='table cb-srs-pnts')
th=soup.find('th',class_='cb-srs-pnts-th text-left')
# print(th.text)
td=soup.findAll('td',class_='cb-srs-pnts-th')
Headers=['Teams']
Teams=[]
for i in td:
    Headers.append(i.text)
Headers.insert(-1,'Pts')
teamtd=soup.findAll('td',class_='cb-srs-pnts-name')
# print(teamtd)
for i in teamtd:
    Teams.append(i.text)

# print(Headers)
# print(Teams)
teampoints=soup.findAll('td',class_='cb-srs-pnts-td')

# print(teampoints)
MatchTabel=[]
for i in teampoints:
    MatchTabel.append(i.text)
MatchTabel=np.array(MatchTabel).reshape((8,7))
# print(MatchTabel)


mat=[MatchTabel[i][0] for i in range(8)]
won=[MatchTabel[i][1] for i in range(8)]
lost=[MatchTabel[i][2] for i in range(8)]
tied=[MatchTabel[i][3] for i in range(8)]
nr=[MatchTabel[i][4] for i in range(8)]
pts=[MatchTabel[i][5] for i in range(8)]
nrr=[MatchTabel[i][6] for i in range(8)]
d={
    'Teams':Teams,
    'Mat':mat,
    'Won':won,
    'Lost':lost,
    'Tied':tied,
    'Nr':nr,
    'Pts':pts,
    'Nrr':nrr
}
df=pd.DataFrame(d,index=[1,2,3,4,5,6,7,8])
print(df.to_string(index=False))
print(df)
oppo=soup.findAll('th',class_='text-left')
details=soup.findAll('td',class_='text-left')
opponent=[]
matchno=[]
date=[]
result=[]
c=1
pd.set_option('display.max_rows',112)
for i in details:
    st=i.text
    if st.startswith('Ch') or st.startswith('Mu') or st.startswith('Ro') or st.startswith('Ra') or st.startswith('De') or st.startswith('Su') or st.startswith('Ki') or st.startswith('Ko') :
        # print(st)
        opponent.append(st)
    elif st.endswith('Match'):
        # print(st)
        matchno.append(st)
    elif st[:3].rstrip(' ').isnumeric() :
        # print(st)
        date.append(st)
    elif st.startswith('Lo') or st.startswith('Wo') or st.startswith('Match'):
        # print(st)
        result.append(st)
    else:
        # print('Need to play')
        result.append('Need to play')
    c+=1
self_=[]
for i in range(len(Teams)):
    for j in range(14):
        self_.append(Teams[i])
# print(self_)
d1={
            'Team'    :self_,
            'Opponent':opponent,
            'MatchNo' :matchno,
            'Date'    :date,
            'Result'  :result,
           
}
df2=pd.DataFrame(d1,index = [ j for i in range(len(Teams)) for j in range(1,15) ])
# print(df2.to_string(index=False))
print(df2)
with open('IPL_Points.txt','w') as f:
    f.write(df.to_string())
    f.write(df2.to_string())