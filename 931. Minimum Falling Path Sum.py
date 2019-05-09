931. Minimum Falling Path Sum

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        
        # 只能向下或者斜着走
        # 边界条件有时是inf
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                topleft=A[i-1][j-1] if j-1>=0 else float('inf')
                topright=A[i-1][j+1] if j+1<=len(A[0])-1 else float('inf')
                A[i][j]+=min(topleft,topright,A[i-1][j])# 只能向下或者斜着走
        
        return min(A[-1])
                
                
