'''Program on python'''
def oddtuples(a_tup):
    '''aTup: a tuple returns: tuple, every other element of aTup.'''
    for i in range(0, len(a_tup), 2):
        print(a_tup[i])

def main():
	#Main program
    data = input()
    data = data.split(",")
    a_tup = ()
    for j in range(len(data)):
        a_tup += (int(data[j]),)
    print(oddtuples(a_tup))

if __name__ == "__main__":
    main()
