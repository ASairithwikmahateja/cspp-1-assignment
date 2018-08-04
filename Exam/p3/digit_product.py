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
    while int_input > 0:
        temp = int_input%10
        prod = prod*temp
        int_input = int_input//10
    print(prod)
if __name__ == "__main__":
    main()
