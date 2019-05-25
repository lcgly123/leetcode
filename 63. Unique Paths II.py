63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        r,c=len(obstacleGrid),len(obstacleGrid[0])
        
        obstacleGrid[0][0]=1 
        flag=1
        for i in range(1,r):
            if obstacleGrid[i][0]==1:
                flag=0
            obstacleGrid[i][0]=flag
        
        flag=1
        for j in range(1,c):
            if obstacleGrid[0][j]==1:
                flag=0
            obstacleGrid[0][j]=flag
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
            
        
        
        # 在路径中加了一些障碍物，还是用动态规划Dynamic Programming来解，不同的是当遇到为1的点，将该位置的dp数组中的值清            #零
        
#         r,c=len(obstacleGrid),len(obstacleGrid[0])
#         if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
#             return 0
#         obstacleGrid[0][0]=1-obstacleGrid[0][0]# 一个技巧，下面会用到
#         for i in range(1,r):
#             obstacleGrid[i][0]=(1-obstacleGrid[i][0])*obstacleGrid[i-1][0]# 一个技巧
#         for i in range(1,c):
#             obstacleGrid[0][i]=(1-obstacleGrid[0][i])*obstacleGrid[0][i-1]
#         for i in range(1,r):
#             for j in range(1,c):
#                 obstacleGrid[i][j]=(obstacleGrid[i-1][j]+obstacleGrid[i][j-1])*(1-obstacleGrid[i][j])
                
#         return obstacleGrid[-1][-1]
        
        
