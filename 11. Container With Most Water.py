11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        res=0# 有点像贪心搜索
        while(l<r):
            h=min(height[l],height[r])
            res=max(res,h*(r-l))# 储水量
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return res


        
#         pleft=0
#         pright=len(height)-1
#         output=0
        
#         while(pleft!=pright):
#             h=min(height[pleft],height[pright])
#             curr_max=h*(pright-pleft)
#             output=max(curr_max,output)
#             if height[pleft]>height[pright]:
#                 pright-=1
#             else:
#                 pleft+=1
                
#         return output
        
        
        
        
