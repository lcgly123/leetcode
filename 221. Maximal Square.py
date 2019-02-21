221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4





class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        m,n=len(matrix),len(matrix[0])
        A=[[1 if matrix[i][j]=='1' else 0  for j in range(n)]for i in range(m)]# 用来DP
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    A[i][j]=min(A[i-1][j-1],A[i][j-1],A[i-1][j])+1# 本题的递推公式，NB
                else:
                    A[i][j]=0
                    
        return max([max(i) for i in A])**2
