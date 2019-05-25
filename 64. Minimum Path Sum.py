64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for  i in range(1,len(grid)):
            grid[i][0]=grid[i-1][0]+grid[i][0]
        for j in range(1,len(grid[0])):
            grid[0][j]=grid[0][j-1]+grid[0][j]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
                
        return grid[-1][-1]
                
        
        
        
        
#         # 动态规划也挺好用的
#         r,c=len(grid),len(grid[0])
#         for i in range(1,r):
#             grid[i][0]=grid[i][0]+grid[i-1][0]# 一个技巧
#         for i in range(1,c):
#             grid[0][i]=grid[0][i]+grid[0][i-1]
#         for i in range(1,r):
#             for j in range(1,c):
#                 grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
                
#         return grid[-1][-1]
