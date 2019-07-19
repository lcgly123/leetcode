59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A=[[0]*n for _ in range(n)]
        flag=[[0]*n for _ in range(n)] # 更加普适
        dx=0
        dy=1
        x,y=0,0
        
        for i in range(n*n):
            A[x][y]=i+1
            flag[x][y]=1
            if flag[(x+dx)%n][(y+dy)%n]==1:# 试探一下
                dx,dy=dy,-dx # 撞了就顺时针旋转90度，有用
            x+=dx
            y+=dy
        
        return A
