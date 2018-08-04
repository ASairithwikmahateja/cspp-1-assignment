"""Write a python program to find the cube root of the given number"""
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
def main():
    '''Program starts here'''
    cube = int(input())
    epsilon = 0.01
    guess = 1
    increment = 0.001
    while abs(guess**3-cube) >= epsilon:
        guess += increment
    if abs(guess**3-cube) >= epsilon:
        print(cube, "is not a perfect cube")
    else:
        print(cube, "is a perfect cube")
if __name__ == "__main__":
    main()
