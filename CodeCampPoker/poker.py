'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    a_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    t_l = []
    for card in hand:
        t_l.append(a_dict[card[0]])
    t_l.sort()

    for item in range(len(t_l)-1):
        if int(t_l[item])-int(t_l[item+1]) != -1:
            return False
        return True
    # if all(True if i is "A2345" else False for i,v in hand):

def is_four_of_a_kind(hand):
    '''Four of a kind'''
    a_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    t_l = []
    cnt = 0
    for card in hand:
        t_l.append(a_dict[card[0]])
        t_l.sort()
    for item in range(len(t_l)-1):
        if int(t_l[item])-int(t_l[item+1]) == 0:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0
def is_three_of_a_kind(hand):
    '''Three of a kind'''
    a_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    t_l = []
    cnt = 0
    for card in hand:
        t_l.append(a_dict[card[0]])
        t_l.sort()
    for item in range(len(t_l)-1):
        if int(t_l[item])-int(t_l[item+1]) == 0:
            cnt += 1
            if cnt == 2:
                return True
        else:
            cnt = 0

def is_two_pair(hand):
    '''Three of a kind'''
    a_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    t_l = []
    cnt = 0
    for card in hand:
        t_l.append(a_dict[card[0]])
        t_l.sort()
    for item in t_l:
        if t_l.count(item) == 2:
            cnt += 1
            if cnt == 4:
                return True
        else:
            cnt = 0


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suit_set = set()
    for card in hand:
        suit_set.add(card[1])
    return len(suit_set) == 1

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    if hand is is_flush(hand) and is_straight(hand):
        return 4
    # best hand of these 3 would be a straight flush with the return value 4
    if hand is is_four_of_a_kind(hand):
        return 3
    # the second best would be a four of a kind with the return value 3
    if hand is is_flush(hand):
        return 2
    # the second best would be a flush with the return value 2
    if hand is is_straight(hand):
        return 1
    # third would be a straight with the return value 1
    return 0
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
