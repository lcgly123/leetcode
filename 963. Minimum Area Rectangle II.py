963. Minimum Area Rectangle II

Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:



Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

包括斜边

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        res=float('inf')
        
        st=  {(x, y) for x, y in points} # 集合
        n=len(points) 
        for i in range(n-2):
            x1, y1 = points[i]
            for j in range(i + 1, n-1):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    if not (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) and (x3 + (x2 - x1), y3 + (y2 - y1)) in st:# 两边的内积判断是否直角，后一个判断是否平行
                        res = min(res, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)# 就是求面积
        return res if res < float("inf") else 0
