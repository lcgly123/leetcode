939. Minimum Area Rectangle

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2



class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        res=float('inf')
        seen=set()
        for x1,y1 in points:
            for x2,y2 in seen:# 对角点，总会循环到的，斜的矩形不管
                if (x1,y2) in seen and (x2,y1) in seen:
                    area=abs(x2-x1)*abs(y2-y1)
                    # print(area)
                    res=min(res,area)
                    
            seen.add((x1,y1))
            
        return res if res!=float('inf') else 0
        
        
