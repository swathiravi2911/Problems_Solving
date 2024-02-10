class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        for i in range(N-1):
            for j in range(i+1, N):
                if A[i] + A[j] == B:
                    return 1
        return 0

'''
Since the input size is 10^4, O(n^2) solution works
T.C = o(n^2)
S.c = O(1) auxiliary space
    O(n) input space
'''