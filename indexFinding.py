l=[[[1,3,2] ,2,[1,3]],[1,3,2]]

def index_all(searching,item):
    indices=[]
    for i in range(len(searching)):
        if searching[i] == item :
            indices.append([i])
        elif isinstance(searching[i],list):
            for index in index_all(searching[i],item):
                indices.append([i]+index)
    return indices

print(index_all(l,1))
print(l[0])