from copy import deepcopy

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        max_i = len(M)
        max_j = len(M[0])
        res = deepcopy(M)
        for i in range(max_i):
        	for j in range(max_j):
        		neighbors = [M[i_][j_] 
        		    for i_ in (i-1, i, i+1) 
        		    for j_ in (j-1, j, j+1)
        		    if 0 <= i_ < max_i and 0 <= j_ <max_j
        		]
        		res[i][j] = sum(neighbors)//len(neighbors)
        return res

A = Solution()
A.imageSmoother([[1,1,1], [1,0,1], [1,1,1]])
