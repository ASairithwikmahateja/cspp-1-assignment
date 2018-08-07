"""Write a python program for factorial"""
def factorial(n_i):
    '''n is positive Integer
    returns: a positive integer, the factorial of n.'''
    if n_i in (0, 1):
        return 1
    res = n_i*factorial(n_i-1)
    return res

def main():
    """Main program"""
    a_inpu = input()
    print(factorial(int(a_inpu)))
if __name__ == "__main__":
    main()
