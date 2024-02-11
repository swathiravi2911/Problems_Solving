import math
# class Solution:
#     def solve(self, A, B):
#         N = len(A)

#         # create empty prefix and suffix arrays
#         pf_arr = [0 for x in range(N)]
#         sf_arr = [0 for x in range(N)]

#         # prefix_sum & suffix_sum array
#         pf_arr[0] = A[0]
#         sf_arr[N-1] = A[N-1]
#         for i in range(1, N):
#             pf_arr[i] = pf_arr[i-1] + A[i]
#             sf_arr[N-1-i] = sf_arr[N-i] + A[N-1-i]
        
#         # find the max sum
#         max_sum = -math.inf
#         for j in range(B+1):
#             if j == 0:
#                 sum = sf_arr[N-B+j]
#             elif j == B:
#                 sum = pf_arr[j-1]
#             else:
#                 sum = pf_arr[j-1] + sf_arr[N-B+j]
#             if sum > max_sum:
#                 max_sum = sum
#         return max_sum

# Other way of writing the same

class Solution:
    def solve(self, A, B):
        N = len(A)

        # creating empty arrays
        pf_sum = [0 for i in range(N)]   # [0] * N
        sf_sum = [0 for i in range(N)]

        # creating prefix sum and sufix sum
        pf_sum[0] = A[0]
        sf_sum[N-1] = A[N-1]

        for i in range(1, N):
            pf_sum[i] = pf_sum[i-1] + A[i]
        
        for i in range(N-2, -1, -1):
            sf_sum[i] = sf_sum[i+1] + A[i]
        
        # finding the max
        '''
        considering corner scenarios of 
        sum of B elements from left = pf_sum[B-1]
        and sum of B elements from right = sf_sum[N-B]
        '''
        ans = max(pf_sum[B-1], sf_sum[N-B])

        for i in range(1, B):
            sum = pf_sum[i-1] + sf_sum[N-B+i]
            ans = max(ans, sum)
        return ans



if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([5, -2, 3, 1, 2], 3))
    print(sol.solve([ 2, 3, -1, 4, 2, 1 ], 4))
    print(sol.solve([2,3,4,3,4,4,1], 6))


            