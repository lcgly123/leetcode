885. Spiral Matrix III

On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid. 


 

Example 1:

Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]


 

Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]



class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        stepsize=1
        sign=1
        
        i,j=r0,c0
        res = [[r0, c0]]
        
        # 有用
        while(len(res)<R*C):
            for _ in range(stepsize):
                j+=sign# 先向右
                if 0<=i<R and 0<=j<C:
                    res.append([i,j])
            
            for _ in range(stepsize):
                i+=sign# 再向下
                if 0<=i<R and 0<=j<C:
                    res.append([i,j])
            
            stepsize+=1
            sign*=-1
        
        return res
            
