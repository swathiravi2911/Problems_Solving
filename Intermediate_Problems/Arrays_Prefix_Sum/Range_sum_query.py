class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        # create the prefix sum array
        N = len(A)
        pf_sum = [0] * N
        pf_sum[0] = A[0]
        for i in range(1, N):
            pf_sum[i] = pf_sum[i-1] + A[i]
        ans = []
        for j in range(len(B)):
            l = B[j][0]
            r = B[j][1]
            if l == 0:
                ans.append(pf_sum[r])
            else:
                range_sum = pf_sum[r] - pf_sum[l-1]
                ans.append(range_sum)
        return ans

'''
T.C = O(N) + O(Q) - whichever the greater
S.C = O(N) for prefix array

Constraints:
1 <= N, M <= 10(5) 10 power 5
1 <= A[i] <= 109 10 power 9
0 <= L <= R < N

array size of 10 power 5 -> 10**5
lets say each element is 10 power 9 -> 10**9
sum = 10**9 + 10**9 + .... + 10**9 -> 10**5 times
sum = (10**9) * (10**5)
sum = 10**14

Max number can be stored in int datatype is  -2*(10**9) to  2*(10**9)-1
to store the above number we need to use long datatype because
long accepts -(2**3)*(10**18) to (2**3)*(10**18)-1


'''