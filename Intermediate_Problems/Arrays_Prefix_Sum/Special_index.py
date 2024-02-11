class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)

        # create empty even_sum and odd_sum array
        pf_even = [0 for x in range(N)]
        pf_odd = [0 for x in range(N)]

        # create pf_even and pf_odd array
        pf_even[0] = A[0]
        pf_odd[0] = 0
        for i in range(1, N):
            if i % 2 == 0: # for even indicies
                pf_even[i] = pf_even[i-1] + A[i]
                pf_odd[i] = pf_odd[i-1]
            else:
                pf_odd[i] = pf_odd[i-1] + A[i]
                pf_even[i] = pf_even[i-1]
        
        # modified pf_even and pf_odd for every index of A
        count = 0
        for i in range(N):
            if i == 0:
                evenSum = pf_odd[N-1]
                oddSum = pf_even[N-1] - pf_even[0]
            else:
                evenSum = pf_even[i-1] + pf_odd[N-1] - pf_odd[i]
                oddSum = pf_odd[i-1] + pf_even[N-1] - pf_even[i]

            # validate whether the sum is equal
            if evenSum == oddSum:
                count += 1
            print(i, count)
            
        return count

if __name__ == "__main__":
    sol = Solution()
   # print(sol.solve([2, 1, 6, 4]))  # 1
    print(sol.solve([1, 1, 1]))



