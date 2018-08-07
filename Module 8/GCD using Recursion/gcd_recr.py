"""Write a Python function, gcdRecur(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b."""
def gcdrecur(a, b):
    '''a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.'''
    if a%b == 0:
    	return b
    else:
    	rmn = a%b
    	a = b
    	b = rmn
    	return gcdrecur(a, b)

def main():
    data = input()
    data = data.split()
    print(gcdrecur(int(data[0]), int(data[1])))

if __name__== "__main__":
    main()