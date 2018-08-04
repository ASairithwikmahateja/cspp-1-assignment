'''Write a python program to find the square root of the given number
using approximation method'''

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''Program starts here'''
    s_num = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon_ = 0.01
    # your code starts here
    low_ = 1
    high_ = s_num
    ans_ = (high_+low_)/2.0
    numguesses_ = 0
    while abs(ans_**2 - s_num) >= epsilon_:
        print(' low = '+str(low_)+' high = '+str(high_)+' ans = '+str(ans_))
        numguesses_ += 1
        if ans_**2 < s_num:
            low_ = ans_
        else:
            high_ = ans_
        ans_ = (high_+low_)/2.0
    print(' numGuesses = '+str(numguesses_))
    print(str(ans_)+' is close to square root of '+str(s_num))
if __name__ == "__main__":
    main()
