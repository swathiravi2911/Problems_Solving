def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    l = list(map(int,input().strip().split()))
    global a
    a = [l[i] for i in range(1, l[0]+1)]
    b = int(input())
    n = len(a)
    b = b%n
    reverseArray(a, 0, n-1)
    reverseArray(a, 0, b-1)
    reverseArray(a, b, n-1)
    for k in a:
        print(k, end = ' ')
    # for _ in range(b):
    #     temp = a[n-1]
    #     for i in range(n-2, -1, -1):
    #         a[i+1] = a[i]
    #     a[0] = temp
    # for j in a:
    #     print(j, end = ' ')
    # #print(a)
    # #print(' '.join(str(e) for e in a))
    # return 0

def reverseArray(a, start_index, end_index):
    i = start_index
    j = end_index
    while (i < j):
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

if __name__ == '__main__':
    main()


'''
T.C = o(n) + o(n) + o(n) = o(n)
S.C = o(1) - auxiliary space
    o(n) - input space

'''