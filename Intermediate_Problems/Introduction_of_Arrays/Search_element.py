def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for i in range(T):
        A = int(input())
        L = list(map(int,input().split()))
        B = int(input())
        R = 0
        for j in L:
            if j == B:
                R = 1
                break
        print(R)  
    return 0

if __name__ == '__main__':
    main()