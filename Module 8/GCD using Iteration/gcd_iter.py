"""Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.This function takes in two numbers and returns one number."""
def gcditer(a, b):
    '''a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.'''
    for i in range(1, a+1):
        if a%i == 0 and b%i == 0:
        	gcd = i
    return gcd 

def main():
    data = input()
    data = data.split()
    print(gcditer(int(data[0]), int(data[1]))) 

if __name__ == "__main__":
    main()