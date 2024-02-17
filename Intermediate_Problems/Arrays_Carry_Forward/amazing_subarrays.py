class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        if N == 0: return 0
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # idea is each element in array make N-i subarrays
        for i in range(N):
            if A[i] in vowels:
                count = (count + (N-i) % 10003) % 10003
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve('ABEC'))