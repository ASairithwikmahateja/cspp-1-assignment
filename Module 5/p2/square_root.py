'''Write a python program to find the square root of the given number'''
def main():
    """Program starts here"""
    sqr = int(input())
    epsilon = 0.01
    guess = 0.0
    increment = 0.001
    num_guesses = 0
    while abs(guess**2-sqr) >= epsilon:
        guess += increment
        num_guesses += 1
    print("num_guesses =", num_guesses)
    if abs(guess**2-sqr) >= epsilon:
        print("Failed on square root of", sqr)
    else:
        print(guess, "is close to square root of", sqr)
if __name__ == "__main__":
    main()
