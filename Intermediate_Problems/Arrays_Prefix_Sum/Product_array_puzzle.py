class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)
        #prefix and sufix multiplication array
        pf_mul = [0] * N
        sf_mul = [0] * N

        pf_mul[0] = A[0]
        sf_mul[N-1] = A[N-1]
        for i in range(1, N):
            pf_mul[i] = pf_mul[i-1] * A[i]
        print(pf_mul)
        for i in range(N-2, -1, -1):
            sf_mul[i] = sf_mul[i+1] * A[i]
        print(sf_mul)
        
        output = [0] * N
        output[0] = sf_mul[1]
        output[N-1] = pf_mul[N-2]
        for i in range(1, N-1):
            output[i] = pf_mul[i-1] * sf_mul[i+1]
        return output

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([1,2,3,4,5]))

'''
Time complexity = O(N)+O(N)+O(N) = O(N)
Space complexity = O(N)+O(N)+O(N) = O(N)

'''