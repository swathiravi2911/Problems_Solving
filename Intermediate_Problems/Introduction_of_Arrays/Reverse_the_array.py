class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        B = list(A)
        N = len(B)
        i = 0
        j = N - 1
        ans = []
        ans_new = []
        while (i < j):
            B[i], B[j] = B[j], B[i]
            i, j = i+1, j-1
        return B

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve((1,2,3,4,5)))

"""
Other ways
print('Python_reverse',B[::-1])
for k in range(N-1,-1,-1):
    ans.append(B[k])
print('ans',ans)
for m in range(N):
    ans_new.append(B[N-1-m])
print('ans_new: ',ans_new)
"""

'''
T.C = N/2 iterations = O(n)
S.C = B+i+j = O(n)+O(1)+O(1) = O(n) auxiliary space
    = O(n) input space

'''