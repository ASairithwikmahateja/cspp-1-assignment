inp= "apple 1\nb 2\nc 3\na 6\nb 3\napple 1\nb 2\nc 3\na 6\nb 3\na 1\nb 2\nc 3\na 6\nb 3"

inp=inp.split("\n")
print(inp)
dictr ={}
for i in inp:
    key_ = i.split(" ")[0]
    value_ =  i.split(" ")[1]
    if key_ not in dictr:
        dictr[key_]=list(value_)
    else:
        dictr[key_].append(value_)
print(dictr)
