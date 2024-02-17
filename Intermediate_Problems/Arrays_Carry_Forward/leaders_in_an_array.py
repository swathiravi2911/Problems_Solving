class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        leaders = []
        max_from_right = A[N-1]
        leaders.append(A[N-1])
        for i in range(N-2, -1, -1):
            if A[i] > max_from_right:
                leaders.append(A[i])
                max_from_right = A[i]
        return leaders

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([16, 17, 4, 3, 5, 2]))
