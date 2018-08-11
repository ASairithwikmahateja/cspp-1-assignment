inp= "a 1\nb 2\nc 3\na 6\nb 3\na 1\nb 2\nc 3\na 6\nb 3\na 1\nb 2\nc 3\na 6\nb 3"

inp=inp.split("\n")
print(inp)
dictr ={}

for i in inp:
    if i.split(" ")[0] not in dictr:
        dictr[i.split(" ")[0]]=list(i.split(" ")[1])
    else:
        dictr[i.split(" ")[0]].append(i.split(" ")[1])

print(dictr)

        
