l=[[1,2],[3,4],[5,6,7],'abc','defgh',1234,56789,(1,2,3)]

# reverse the list l
l.reverse()
result = []

#reverse every inner list and string
for i in l:
    if type(i) is list:
        i.reverse()
        result.append(i)
    elif type(i) is tuple:
    	tmp=list(i)
    	tmp.reverse()
    	result.append(tuple(tmp))
    elif type(i) is str:
        result.append(i[::-1])
    elif type(i) is int:
        strr = str(i)
        result.append(int(strr[::-1]))
print(result)
