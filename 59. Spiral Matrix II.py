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
        x,y=0,0
        dx,dy=0,1
        for i in range(n*n):
            A[x][y]=i+1
            if A[(x+dx)%n][(y+dy)%n]:
                dx,dy=dy,-dx
            x+=dx
            y+=dy
        return A
        

        
        
#         A=[[0 for i in range(n)] for i in range(n)]
#         x,y,dx,dy=0,0,0,1
#         for i in range(n*n):
#             A[x][y]=i+1
#             if A[(x+dx)%n][(y+dy)%n]:#就是走到头了（循环了），有用
#                 dx,dy=dy,-dx# 撞了就顺时针旋转90度，有用
#             x+=dx
#             y+=dy
            
#         return A
