'''Write a python program'''
def main():
    """Program starts here"""
    num = int(input())
    fact = 1
    for i in range(0, num, 1):
        fact = fact*i
    print(fact)
if __name__ == "__main__":
    main()
