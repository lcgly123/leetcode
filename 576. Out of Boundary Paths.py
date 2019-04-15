576. Out of Boundary Paths

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        
        dp={}
        def dfs(x,y,N):
            if (x,y,N) in dp:# 只有x，y无法确定该点有多少种方式出去，边界都确定不了
                return dp[(x,y,N)]
            if not(0<=x<m and 0<=y<n):# 出界return1
                return 1
            if N==0:# 这个一定没出界
                return 0
            
            res=dfs(x+1,y,N-1)+\
                dfs(x-1,y,N-1)+\
                dfs(x,y+1,N-1)+\
                dfs(x,y-1,N-1)
            dp[(x,y,N)]=res%(1e9+7)# 这也要mod
            return res
        
        return dfs(i,j,N)%(1e9+7)
        

 
