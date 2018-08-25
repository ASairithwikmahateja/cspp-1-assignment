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
    		dictfreq[i] = 1
    	else:
    		dictfreq[i] += 1
    print(dict(zip(dictfreq.keys(),dictfreq.values())))

def main():
    '''
    Main Function
    '''
    n_l = int(input())
    lst = []
    for i in range(n_l):
        line = input().split(" ")
        lst.append(line)
    tokenize(lst)

if __name__ == '__main__':
    main()
