import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        # find the max
        max_ele = -math.inf
        for ele in A:
            if ele > max_ele:
                max_ele = ele
        count = 0
        for ele in A:
            count += max_ele - ele
        return count