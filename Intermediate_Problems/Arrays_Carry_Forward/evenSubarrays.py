class Solution:
    def solve(self, A):
        return 'YES' if (len(A) % 2 == 0 and A[0] % 2 == 0 and A[-1] % 2 == 0) else 'NO'

        
        # N = len(A)
        # if N < 4: return 'NO'
        # if N % 2 != 0: return 'NO'
        # if A[0] % 2 != 0: return 'NO'
        # if A[N-1] % 2 != 0: return 'NO'
        # count_of_subarrays = 0
        # # A[0] is even, so start to search from 1
        # i = 0
        # while (i < N):
        #     if A[i] % 2 == 0:
        #         for j in range(i+1, N):
        #             if A[j] % 2 == 0:
        #                 length_of_subarray = j - i + 1
        #                 if length_of_subarray % 2 != 0:
        #                     return 'NO'
        #                 else:
        #                     count_of_subarrays += 1
        #                     i = j + 1
        #                     break
        #     else:
        #         return 'NO'
        # return 'YES' if count_of_subarrays > 1 else 'NO'


if __name__ == "__main__":
    sol = Solution()
    #print(sol.solve([2, 4, 8, 6]))
    #print(sol.solve([2, 4, 8, 7, 6]))
    print(sol.solve([978,847,95,729,778,586,188,782,813,870,871,940,312,693,580,101,760,837,564,633,680,155,241,374,682,290,850,601,433,922,773,959,530,290,990,50,516,409,868,131,664,851,721,880,20,450,745,387,787,823,392,242,674,347,65,135,819,324,651,678,139,940]))





