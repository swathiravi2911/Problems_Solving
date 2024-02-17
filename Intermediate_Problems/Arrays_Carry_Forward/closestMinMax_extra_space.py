import math
class Solution:
    def solve(self, A):
        N = len(A)
        Amin = min(A)
        Amax = max(A)

        #edge case scenario
        if Amin == Amax: return 1
        # to hold nearest max index from 0 to N-1
        pf_array = [0] * N
        # to hold nearest max index from N-1 to 0
        sf_array = [0] * N
        # if A[0] == Amax:
        #     pf_array[0] = 0
        # else:
        #     pf_array[0] = -math.inf
        pf_array[0] = 0 if A[0] == Amax else -math.inf
        sf_array[N-1] = N-1 if A[N-1] == Amax else -math.inf
        for i in range(1, N):
            if A[i] == Amax:
                pf_array[i] = i
            else:
                pf_array[i] = pf_array[i-1]
        for i in range(N-2, -1, -1):
            if A[i] == Amax:
                sf_array[i] = i
            else:
                sf_array[i] = sf_array[i+1]
        
        # Traverse array from 0 to N-1, stop at min and use pf_array
        # and sf_array to find the nearest max
        min_length = N
        for i in range(N):
            if A[i] == Amin:
                if (pf_array[i] != -math.inf):
                    min_length = min((i - pf_array[i] + 1), min_length)
                if (sf_array[i] != -math.inf):
                    min_length = min((sf_array[i] - i + 1), min_length)
        return min_length

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([343,291,963,165,152]))
    print(sol.solve([814,761,697,483,981]))



        
        
