417. Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def dfs(x,y,res,pre):
            if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]) or res[x][y]==1 or matrix[x][y]<pre:# 同时检查是否走过，NB
                return
            res[x][y]=1
            dfs(x-1,y,res,matrix[x][y])
            dfs(x+1,y,res,matrix[x][y])
            dfs(x,y-1,res,matrix[x][y])
            dfs(x,y+1,res,matrix[x][y])
        if matrix==[]:
            return []
        
        m=len(matrix)
        n=len(matrix[0])
        
        P=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        A=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        # 看从边界能走到哪，NBNB！！
        for i in range(len(matrix)):
            dfs(i,0,P,0)
            dfs(i,n-1,A,0)
        for i in range(len(matrix[0])):
            dfs(0,i,P,0)
            dfs(m-1,i,A,0)
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if P[i][j]+A[i][j]==2:#不能 P[i][j]==A[i][j]因为会有都为0
                    res.append([i,j])
        return res
                
        
        
        
        
        
        #会超时
#         def dfs_P(x,y,path):
#             if [x,y] in path:
#                 return
#             if x-1<0 or y-1<0:
#                 return True
#             if x+1!=len(matrix):
#                 if matrix[x+1][y]<=matrix[x][y]:
#                     ans=dfs_P(x+1,y,path+[[x,y]])
#                     if  ans==True:
#                         return True
#             if x-1!=-1:
#                 if matrix[x-1][y]<=matrix[x][y]:
#                     ans=dfs_P(x-1,y,path+[[x,y]])
#                     if  ans==True:
#                         return True
#             if y+1!=len(matrix[0]):
#                 if matrix[x][y+1]<=matrix[x][y]:
#                     ans=dfs_P(x,y+1,path+[[x,y]])
#                     if  ans==True:
#                         return True
#             if y-1!=-1:
#                 if matrix[x][y-1]<=matrix[x][y]:
#                     ans=dfs_P(x,y-1,path+[[x,y]])
#                     if  ans==True:
#                         return True
                    
#         def dfs_A(x,y,path):
#             if [x,y] in path:
#                 return
#             if x+1==len(matrix) or y+1==len(matrix[0]):
#                 return True
   
#             if x+1!=len(matrix):
#                 if matrix[x+1][y]<=matrix[x][y]:
#                     ans=dfs_A(x+1,y,path+[[x,y]])
#                     if  ans==True:
#                         return True
#             if x-1!=-1:
#                 if matrix[x-1][y]<=matrix[x][y]:
#                     ans=dfs_A(x-1,y,path+[[x,y]])
#                     if  ans==True:
#                         return True
#             if y+1!=len(matrix[0]):
#                 if matrix[x][y+1]<=matrix[x][y]:
#                     ans=dfs_A(x,y+1,path+[[x,y]])
#                     if  ans==True:
#                         return True
#             if y-1!=-1:
#                 if matrix[x][y-1]<=matrix[x][y]:
#                     ans=dfs_A(x,y-1,path+[[x,y]])
#                     if  ans==True:
#                         return True
        
#         res=[]
#         for x in range(len(matrix)):
#             for y in range(len(matrix[0])):
#                 ans=dfs_P(x,y,[])
#                 if ans==True:
#                     res.append([x,y])
#         # print(res)
#         real_res=[]
#         for x,y in res:
#             ans=dfs_A(x,y,[])
#             if ans==True:
#                     real_res.append([x,y])
          
        
#         return real_res
                    
        
            

