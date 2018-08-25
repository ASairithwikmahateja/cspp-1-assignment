'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def freq(temp):
    '''
    temp function
    '''
    lst = []
    for i in range(temp):
        lst.append("#")
    return lst

def frequency_graph(dictionary):
    '''
    Frequency Graph Function
    '''
    lst = []
    for i in dictionary.keys():
        lst.append(i)
    lst.sort()
    for i in lst:
    	temp = dictionary[i]
    	print(i, "-", freq(temp))  	    

def main():
    '''
    Main Function
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
