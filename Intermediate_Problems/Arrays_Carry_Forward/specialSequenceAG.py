from msilib import sequence


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        count_a = 0
        answer = 0
        for i in range(N):
            if A[i] == 'A':
                count_a += 1
            elif A[i] == 'G':
                answer += count_a
        return answer

    def anotherWay(self, A):
        N = len(A)
        count_g = 0
        answer = 0
        for i in range(N-1, -1, -1):
            if A[i] == 'G':
                count_g += 1
            elif A[i] == 'A':
                answer += count_g
        return answer




if __name__ == "__main__":
    sol = Solution()
    print(sol.solve('ABCGAG'))
    print(sol.solve('GAB'))
    print(sol.anotherWay('ABCGAG'))
    print(sol.anotherWay('GAB'))
