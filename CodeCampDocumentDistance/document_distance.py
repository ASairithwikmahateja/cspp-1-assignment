'''
    Document Distance - A detailed description is given in the PDF
'''
import math

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1.lower()
    dict2.lower()
    dictionary = {}
    word_freq = {}
    list_1 = dict1.split(" ") + dict2.split(" ")
    spl_char = "!@#$%^&*()-_+"
    for i in list_1:
        if i in spl_char:
            list_1.remove(i)
    for i in list_1:
        dictionary[i] = list_1.count(i)
    dict_3 = load_stopwords("stopwords.txt")
    for i in dict_3:
        if i in dictionary:
            del dictionary[i]
    for i in list_3:
        word_freq[i] = [dict1.split(" ").count(i), dict2.split(" ").count(i)]
    numer_n = 0
    denom_n1 = 0
    denom_n2 = 0
    for i in word_freq:
        numer_n = sum(word_freq[i][0]*word_freq[i][1])
        denom_n1 = sum(word_freq[i][0]**2)
        denom_n2 = sum(word_freq[i][1]**2)
    denom_n = math.sqrt(denom_n1)*math.sqrt(denom_n2)
    return numer_n/denom_n

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
