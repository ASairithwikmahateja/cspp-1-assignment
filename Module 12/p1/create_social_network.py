'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
    Social Network
    '''
    redir = {}
    l_data = list(data.split('\n'))
    for i in l_data:
        key_ = i.split(' ')[0]
        value_ = i.split(' ')[2::]
        redir = dict(zip(key_, value_))
    return redir

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        string += input()
        string += '\n'
        i += 1

    print(create_social_network(string))

if __name__ == "__main__":
    main()
