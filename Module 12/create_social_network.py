'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
    Social Network
    '''
    redir = {}
    l_data = list(data.split('\n'))
    #print(l_data)
    s_data = ''.join(l_data)
    #print(s_data)
    l = s_data.split(' follows ')
    #print(l)
    key_ = []
    value_ = []
    for i in range(len(l)-1):
        key_ = list(l[i][-1])
        #print(key_)
        tmp_ = l[i+1]
        tmp_ = tmp_.split(",")
        s_tmp = ''.join(tmp_)
        tmp_1 = list(s_tmp)
        #print(s_tmp)
        #print(tmp_1)    
        for j in range(len(tmp_1)):
            value_ = list(tmp_1[j])
            #print(value_)
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
