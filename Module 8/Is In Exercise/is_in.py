'''Write a Python function, isIn(char, aStr)'''
def isin(char_, aStr_):
    '''char: a single character
    aStr: an alphabetized string returns: True if char is in aStr; False otherwise'''
    if len(aStr_) == 0:
        return False
    if len(aStr_) == 1:
        return aStr_ == char_
    if aStr_[len(aStr_)//2] == char_:
        return True
    if aStr_[len(aStr_)//2] > char_:
        return isin(char_, aStr_[0:len(aStr_)//2])
    return isin(char_, aStr_[len(aStr_)//2])

def main():
	'''Main Program'''
	data = input()
	data = data.split()
	print(isin((data[0][0]), data[1]))

if __name__ == "__main__":
    main()
