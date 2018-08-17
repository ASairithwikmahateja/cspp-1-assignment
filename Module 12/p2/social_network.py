'''
    This is a continuation of the social network problem
    There are 3 functions below that have to be completed
    Note: PyLint score need not be 10/10 for this assignment. We expect 9.5/10
'''

def follow(network, arg1, arg2):
    '''
    follow
    '''
    if arg2 not in network[arg1]:
        network[arg1].append(arg2)
    return network

def unfollow(network, arg1, arg2):
    '''
    unfollow
    '''
    if arg2 in network[arg1]:
        network[arg1].remove(arg2)
    return network

def delete_person(network, arg1):
    '''
    delete
    '''
    if arg1 in network.keys():
        network.delete(arg1)
    return network

def main():
    '''
        handling testcase input and printing output
    '''
    network = eval(input())
    lines = int(input())
    for i in range(lines):
        i += 1
        line = input()
        output = line.split(" ")
        if output[0] == "follow":
            network = follow(network, output[1], output[2])
        elif output[0] == "unfollow":
            network = unfollow(network, output[1], output[2])
        elif output[0] == "delete":
            network = delete_person(network, output[1])

    print(network)

if __name__ == "__main__":
    main()
