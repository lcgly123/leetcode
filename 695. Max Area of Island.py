695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # memo不能防止来回递归，防止来回递归要么用visit，要么改值（方便）
        # memo就是dp，从不同的路径来到i，j迅速返回，可以减少搜索量
        # 如果可以重复来到一个地方就用memo，不能重复来到一个地方就改值
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]):
                if grid[i][j]!=1:
                    return 0
                grid[i][j]=-1
                sm=1
                move=[(-1,0),(0,-1),(0,1),(1,0)]
                for di,dj in move:
                    sm+=dfs(i+di,j+dj)
                return sm
            else:
                return 0
        
        memo={}
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res=max(res,dfs(i,j))
                    
        return res
                    
                

