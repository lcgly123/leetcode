542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def bfs(x,y):
            queen=[(x,y)]
            seen=[(x,y)]
            step=1
            while(queen):
                new=[]
                for x,y in queen:
                    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                        if 0<=x+dx<len(matrix) and 0<=y+dy<len(matrix[0]) and (x+dx,y+dy) not in seen:
                            if matrix[x+dx][y+dy]==0:
                                return step
                            new.append((x+dx,y+dy))
                            seen.append((x,y))
                step+=1
                queen=new
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    matrix[i][j]=bfs(i,j)
        return matrix
        
        
        
#         # 太恶心了，不如bfs
#         # DP NB，双向DP NB
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]!=0:
#                     matrix[i][j]=float('inf')
#                     if i>0 and matrix[i][j]>matrix[i-1][j]:# 这个一定会中
#                         matrix[i][j]=matrix[i-1][j]+1
#                     if j>0 and matrix[i][j]>matrix[i][j-1]:# 这个其实是和上面比较一下哪个更小
#                         matrix[i][j]=matrix[i][j-1]+1
                        
#         for i in range(len(matrix)-1,-1,-1):
#             for j in range(len(matrix[0])-1,-1,-1):
#                 if matrix[i][j]!=0:
#                     if i<len(matrix)-1 and matrix[i][j]>matrix[i+1][j]:# 选一个更小的
#                         matrix[i][j]=matrix[i+1][j]+1
#                     if j<len(matrix[0])-1 and matrix[i][j]>matrix[i][j+1]:# 这个其实是和上面比较一下哪个更小
#                         matrix[i][j]=matrix[i][j+1]+1
                        
#         return matrix
                
        
