120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i==0:
                    continue
                elif j==0:
                    triangle[i][j]+=triangle[i-1][0]
                elif j==len(triangle[i])-1:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
        return min(triangle[-1])
