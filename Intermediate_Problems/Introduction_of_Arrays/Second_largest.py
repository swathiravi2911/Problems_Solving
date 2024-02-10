import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        first_largest = -math.inf
        second_largest = -math.inf
        for ele in A:
            if ele > first_largest:
                second_largest = first_largest
                first_largest = ele
            elif ele < first_largest and ele > second_largest:
                second_largest = ele
        if second_largest != -math.inf:
            return second_largest
        else:
            return -1

# Scaler solution
class Solution:
    # @param A : list of integers
    # @return an integer
    
    def solve(self, A):
        # This loop calculates the largest element in the list.
        max_elem = -1
        for x in A:
            if x > max_elem:
                max_elem = x
        
        # This loop calculates the second largest element in the list.   
        second_max = -1
        for x in A:
            if x > second_max and x != max_elem:
                second_max = x
        return second_max