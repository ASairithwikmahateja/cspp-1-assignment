"""This function takes in one number and returns one number."""
def sumofdigits(n):
    '''n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    while n > 0:
    	s += n%10
    	return sumofdigits(n/10)
    print(s)

def main():
    a = input()
    print(sumofdigits(int(a)))  

if __name__ == "__main__":
    main()

