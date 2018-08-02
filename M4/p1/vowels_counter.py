#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    str_= input()
    coun_= 0
    for char in str_:
        if char in ('a', 'e', 'i', 'o', 'u'):
            coun_= coun_+ 1
    print (coun_)

if __name__== "__main__":
	main()
