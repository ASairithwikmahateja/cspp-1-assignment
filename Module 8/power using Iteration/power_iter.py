'''Write a Python function, iterPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.'''
def iterpower(base, exp):
    '''base: int or float.
    exp: int >= 0
    returns: int or float, base^exp'''
    res = 1
    while exp >= 1:
        res = res*base
        exp = exp-1
    return res
def main():
    '''main function'''
    data = input()
    data = data.split()
    print(iterpower(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
