rollnumbers=(1,2,3,4)
names = ('a','b','c','d')
mailid= ('a@','b@','c@','d@')
gender = ('m','f','m','f')

result ={}

m = zip(rollnumbers,names,mailid,gender)
print(m)
for i in m:
    result[i[0]]=list(i[:])

print(result)
