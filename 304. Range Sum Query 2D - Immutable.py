304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12



class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        temp=[x[col1:col2+1] for x in self.matrix[row1:row2+1]]# 注意python里的切片只能对list一维切，不像np
        return sum(sum(x) for x in temp)#（sum也只能对一维list求和）
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
