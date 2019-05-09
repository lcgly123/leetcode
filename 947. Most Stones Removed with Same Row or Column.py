947. Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0



class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        # 在二维平面上，我们将石头放置在一些整数坐标点上。
        # 每个坐标点上最多只能有一块石头。
        # 现在，move 操作将会移除与网格上的另一块石头共享一列或一行的一块石头。
        # 我们最多能执行多少次 move 操作？
        # 横或者纵坐标相等的坐标点会互相链接构成一个区域，
        # 问总的有多少个独立的区域。结果是总的石头数减去独立区域数。
        
        
        # 就是找到所有和（i，j）有关的，然后返回1
        def dfs(i,j):
            if (i,j) in seen:
                return 0
            seen.add((i,j))
            for x,y in stones:
                if x==i or y==j:# 表示有联系，有用
                    dfs(x,y)
            return 1
        
        res=0
        seen=set()
        for i,j in stones:
            res+=dfs(i,j)
        
        return len(stones)-res
        
        
