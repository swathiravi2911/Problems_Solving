# using prefix sum

class Solution:
    def solve(self, A):
        # create empty array of same length of original array
        l = len(A)
        PF = [0] * l
        #print(PF)
        # create prefix sum array
        PF[0] = A[0] # prefix sum first element is A's first element, no change in that
        for i in range(l):
            PF[i] = PF[i-1] + A[i]
        
        total_sum = PF[l-1]

        # Handling the leftsum of first element is zero
        if total_sum - A[0] == 0:
            return 0
        
        # leftsum = PF[i-1], rightsum = total_sum - PF[i]
        for i in range(1, l):
            leftsum = PF[i-1]
            rightsum = total_sum - PF[i]
            if leftsum == rightsum:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([-7, 1, 5, 2, -4, 3, 0]))
    print(sol.solve([1, 2, 3]))
    print(sol.solve([-7, 1, 5, 2, -4, -4, 0]))
    print(sol.solve([1, 1, 5, 2, -5, -4, 0]))


        




if __name__ == "__main__":
    sol = Solution()
    sol.solve([1,2,3,4,5,6,7,8,9])