class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B not in A: return -1
        count = 0
        for ele in A:
            if ele > B:
                count += 1
        return count