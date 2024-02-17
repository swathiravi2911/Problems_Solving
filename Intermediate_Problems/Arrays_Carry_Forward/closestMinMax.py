class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        # Find min and max ele in the array
        Amin = A[0]
        Amax = A[0]
        for ele in A:
            if ele < Amin:
                Amin = ele
            if ele > Amax:
                Amax = ele
        
        # find the minimum length
        if Amax == Amin: return 1 
        last_min, last_max = -1, -1
        min_length = N
        for i in range(N):
            if A[i] == Amin:
                last_min = i
            if A[i] == Amax:
                last_max = i
            if (last_min != -1 and last_max != -1):
                min_length = min((abs(last_max - last_min) + 1), min_length)
        return min_length


if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([343,291,963,165,152]))