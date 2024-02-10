# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        max_even = -math.inf
        min_odd = math.inf
        for ele in A:
            if ele % 2 == 0:
                if ele > max_even:
                    max_even = ele
            else:
                if ele < min_odd:
                    min_odd = ele
        return max_even - min_odd