934. Shortest Bridge

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2



class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        # 其实很简单，dfs把岛染黑，bfs找最短路径
        def get_first():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j]:
                        return i,j
        
        # 就是把一个岛染黑
        def dfs(i,j):
            A[i][j]=-1
            queen.append((i,j))
            for x,y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] == 1:
                    dfs(x, y)
        
        queen=[]
        i,j=get_first()
        dfs(i,j)
        
        step=0
        while(queen):
            new=[]
            
            for i,j in queen:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < len(A) and 0 <= y < len(A[0]):
                        if A[x][y]==-1:
                            continue
                        if A[x][y]==1:
                            return step
                        A[x][y]=-1
                        new.append((x,y))
            step+=1
            queen=new
                    
        
