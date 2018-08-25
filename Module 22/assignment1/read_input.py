'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    n = int(input())
    lst = []
    for i in range(n):
    	line = input()
    	lst.append(line)
    for i in lst:
    	print(i)

if __name__ == '__main__':
    main()
