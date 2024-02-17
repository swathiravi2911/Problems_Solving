class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        N = len(A)
        if N == 0: return 0 # if array is empty
        count = 0
        if A[0] == 0:
            count += 1
        for i in range(1, N):
            if A[i] != A[i-1]:
                count += 1
        return count

#logical way of solving it
class Solution1:
    # @params A : list of integers
    # @return an integer
    def bulbs(self, A):
        count = 0
        for i in range(len(A)):
            state = A[i]
            # Based on count(number of times switch on) the current state of bulb changes
            # if odd number of times the switch on, the current state of bulb would be toggled
            # if even, then the state remains same
            if count % 2 == 0:
                state = A[i]
            else:
                state = 1 - A[i]
            
            # based on current state, deside the count
            if state == 0:
                count += 1
        
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.bulbs([0, 1, 0, 1]))
    print(sol.bulbs([1, 1, 1, 1]))
    print(sol.bulbs([0, 0, 0, 0]))
    print(sol.bulbs([]))

    sol1 = Solution1()
    print(sol1.bulbs([0, 1, 0, 1]))
    print(sol1.bulbs([1, 1, 1, 1]))
    print(sol1.bulbs([0, 0, 0, 0]))
    print(sol1.bulbs([]))
