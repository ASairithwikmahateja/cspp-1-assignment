'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(line):
    '''
    Tokenize Function 
    '''
    dictfreq = {}
    for i in line:
    	if i not in dictfreq.keys():
    		dictfreq[i] = 0
    	else:
    		dictfreq[i] += 1
    print(dict(zip(dictfreq.keys(),dictfreq.values())))

def clean_string(string):
    '''
    String Cleaning method
    '''
    spc = "!@#$%^&*() .,"
    str_new = ""
    for i in string:
        if i in spc:
            str_new += ""
        else:
            str_new += i
    return str_new

def main():
    '''
    Main Function
    '''
    n_l = int(input())
    lst = []
    for i in range(n_l):
        line = input().split(" ")
        print(line)
        lst.append(line)
        line = clean_string(lst)
    print(lst)
    tokenize(line)

if __name__ == '__main__':
    main()
