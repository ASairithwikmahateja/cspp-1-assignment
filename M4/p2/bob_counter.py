"""string"""
#Assume s is a string of lower case characters.
def main():
    str_ = input()
    coun_ = 0
    for i in len(str_):
        if "bob" in str_:
            coun_ = coun_+ 1
    print(coun_)  
if __name__ == "__main__":
    main()
