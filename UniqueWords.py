import operator
def uniqueWords(filename):
    totalWords=0
    with open(filename,encoding='utf-8') as f:
        d={}
        for i in f:
            l=i.rstrip('\n').lower().split()
            totalWords+=len(l)
            for j in l:
                d[j]=d.get(j,0)+1
    sorteddict=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    # print(sorteddict)
    print(f'The total words in txt file are {totalWords}')
    top=0
    print('Top 20 Repeated words')
    for i,j in sorteddict.items():
        print(f'{i.rjust(100)}    :    {j} ')
        if top == 20 :
            break
        top+=1
uniqueWords(input('Filename:'))