'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    prod = 1
    prod1 = 1
    if int_input > 0:
        while int_input > 0:
            temp = int_input%10
            prod = prod*temp
            int_input = int_input//10
        print(prod)
    elif int_input < 0:
    	while abs(int_input) > 0:
    		temp = int_input%10
    		prod = prod*temp
    		int_input = int_input//10
    		prod1 = -1*prod
    	print(prod1)
    else:
        print(0)
if __name__ == "__main__":
    main()
