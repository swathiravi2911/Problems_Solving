class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        global n
        n = len(A)
        results = []
        for val in B:
            temp = A[:]
            c = val % n
            self.reverseArray(temp, 0, c-1)
            self.reverseArray(temp, c, n-1)
            self.reverseArray(temp, 0, n-1)
            results.append(temp)
        return results
    
    def reverseArray(self, a, start_index, end_index):
        i = start_index
        j = end_index
        while (i < j):
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

"""
Brute force approach using extra space
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        ans = []
        for i in range(len(B)):
            temp = []
            ind = B[i]%len(A)
            for j in range(ind, len(A)): 
                temp.append(A[j])
            for j in range(ind):
                temp.append(A[j])
            ans.append(temp);
        
        return ans
"""
if __name__ == "__main__":
    A = [1,2,3,4,5]
    B = [2,3]
    sol = Solution()
    print(sol.solve(A, B))
