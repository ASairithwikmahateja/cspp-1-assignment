'''Write a python program'''
def main():
    """Program starts here"""
    s_= input()
    flag_=0
    flag1_=0
    flag2_=0
    flag3_=0
    for char in s_:
        if len(s_) >= 6:
            flag_ = 1
        if char >= 'a' and char <= 'z':
            flag1_ = 1
        if char >= 'A' and char <= 'Z':
        	flag2_ = 1
        if char >= '!' and char <= '/' or char >= ':' and char <= '@':
            flag3_ = 1
    if flag_+flag1_+flag2_+flag3_ >= 4: 
            print("Its a strong password")
    else:
            print("Its not strong password")
if __name__ == "__main__":
    main()
