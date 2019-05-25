74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        l,r=0,len(matrix)*len(matrix[0])-1
        while(l<=r):
            mid=(l+r)//2
            if matrix[mid//len(matrix[0])][mid%len(matrix[0])]==target:
                return True
            elif target<matrix[mid//len(matrix[0])][mid%len(matrix[0])]:
                r=mid-1
            else:
                l=mid+1
        
        return False
                
            
        
        
        
        
        # if len(matrix)==0:
        #     return False
        # if len(matrix[0])==0:
        #     return False
        # for_col=0
        # for r in range(len(matrix)):
        #     if matrix[r][0]==target or matrix[r][-1]==target:
        #         return True
        #     if matrix[r][0]<target and matrix[r][-1]>target:
        #         for_col=r
        #         break
        #     if matrix[r][0]>target:
        #         for_col=r
        #         break
        # print(for_col)
        # if for_col==0:
        #     for x in matrix[for_col]:
        #         if x==target:
        #             return True
        # else:
        #     for x in matrix[for_col]:
        #         if x==target:
        #             return True
        # return False
