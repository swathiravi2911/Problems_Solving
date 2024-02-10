import math
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    l = list(map(int,input().split()))
    a = l[1:]
    max_ele = -math.inf
    min_ele = math.inf
    for ele in a:
        if ele > max_ele:
            max_ele = ele
        if ele < min_ele:
            min_ele = ele
    print(f'{max_ele} {min_ele}')
    return 0

if __name__ == '__main__':
    main()


'''
T.C = O(n)
S.C = O(1)
'''