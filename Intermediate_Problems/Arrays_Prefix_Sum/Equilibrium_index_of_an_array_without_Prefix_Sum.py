'''
without prefix sum, scaler approach
Solution Approach
The idea is to get the total sum of the array first. Then Iterate through the array and keep updating the left sum which is initialized as zero. In the loop, we can get the right sum by subtracting the elements one by one.

1) Initialize leftsum  as 0
2) Get the total sum of the array as sum
3) Iterate through the array and for each index i, do following.
    a)  Update sum to get the right sum.  
           sum = sum - arr[i] 
       // sum is now right sum
    b) If leftsum is equal to sum, then return current index. 
       // update leftsum for next iteration.
    c) leftsum = leftsum + arr[i]
4) return -1 
// If we come out of loop without returning then
// there is no equilibrium index

Time Complexity : O(N)
Space Complexity : O(1)

'''

class Solution:
    def solve(self, A):
        # calculate total_sum
        sum = 0
        for e in A:
            sum += e
        
        # initialize leftsum = 0
        leftsum = 0
        for i in range(len(A)):
            sum = sum - A[i]
            if leftsum == sum:
                return i
            # update left sum for next iteration
            leftsum = leftsum + A[i]
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([-7, 1, 5, 2, -4, 3, 0]))
    print(sol.solve([1, 2, 3]))