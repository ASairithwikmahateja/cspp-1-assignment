'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''
    Dictionary Function
    '''
    lst = []
    for i in dictionary.keys():
        lst.append(i)
    lst.sort()
    for i in lst:
        print(i, "-", dictionary[i])

def main():
    '''
    Main Function
    '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
