"""This function takes in one number and returns one number."""
def sumofdigit(n_i):
    '''n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if n_i == 0:
        return 0
    return n_i%10+sumofdigit(n_i//10)

def main():
    """Program starts here"""
    a_inpu = input()
    print(sumofdigit(int(a_inpu)))

if __name__ == "__main__":
    main()
