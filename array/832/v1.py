class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in range(len(A)):
        # for row in A:
            A[row] = [pixel ^ 1 for pixel in A[row]][::-1]
            # row = [pixel ^ 1 for pixel in row][::-1]
        return A

o = Solution()
r = o.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
print(r)