
def writeDictionary(filename,**kwargs):
    with open(filename,'a+') as f:
        f.write('\n'+str(kwargs))
    return 'Done wrote at '+filename

def readDictionary(filename):
    with open(filename,'r') as f:
        for i in f:
            print(i.rstrip('\n'))
    return 'Done with reading'
d={'name':'Kiran','Age':'20'}
print(writeDictionary(input('filename'),**d))
print(readDictionary(input()))


import pickle

def writeDictionaryPickle(file,dict):
    with open(file,'ab') as f:
        pickle.dump(dict,f)
def readDictionaryPickle(file):
    with open(file,'rb') as f:
        print(pickle.load(f))
writeDictionaryPickle(input(),d)
readDictionaryPickle(input())
