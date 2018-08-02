"""string"""
#Assume s is a string of lower case characters.
def main():
    str_ = input()
    coun_ = 0
    for i in range (0,len(str_)-1,1):
        if str_[i] =='b' and str_[i+1] == 'o' and str_[i+2] == 'b':
            coun_ = coun_+ 1
    print(coun_)  
if __name__ == "__main__":
    main()
