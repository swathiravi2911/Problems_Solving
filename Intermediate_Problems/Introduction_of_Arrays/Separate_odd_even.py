def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd_elements = []
        even_elements = []
        for ele in A:
            if ele % 2 == 0:
                even_elements.append(ele)
            else:
                odd_elements.append(ele)
        for ele in odd_elements: 
            print(ele, end = ' ')
        print('')
        for ele in even_elements: 
            print(ele, end = ' ')
        print('')

    return 0

if __name__ == '__main__':
    main()