#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	s_= input("Enter the string")
	k_= 0
	for char in s_:
		if char in ('a','e','i','o','u'):
			k_= k_+ 1
	print (k_)

if __name__== "__main__":
	main()
