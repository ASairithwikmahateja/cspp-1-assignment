'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    spc = "!@#$%^&*()"
    str_new = ""
    for i in string:
    	if i in spc:
    		str_new += ""
    	else:
    		str_new += i
    print(str_new)

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
