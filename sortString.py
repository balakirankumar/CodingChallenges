import sys

def sortString(s):
    words=s.split()
    words=[i.lower()+i for i in words]
    words.sort()
    words=[i[len(i)//2:] for i in words]
    return ' '.join(words)


print(sortString(sys.argv[1]))