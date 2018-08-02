'''Assume s is a string of lower case characters.
Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    ''' gives longest_substring '''
    str_ = input()
    # the input string
    tstr_ = ""
    for i, item in enumerate(str_):
        cnt_ = 0
        tstr1_ = ""
        tt_ = item
        ji_ = i
        while cnt_ != 1 and ji_ != len(str_):
            if ord(tt_) <= ord(str_[ji_]):
                tt_ = str_[ji_]
                tstr1_ += str_[ji_]
            else:
                cnt_ = 1
            ji_ += 1

        if len(tstr1_) > len(tstr_):
            tstr_ = tstr1_
    print(tstr_)

if __name__ == "__main__":
    main()
