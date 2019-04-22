658. Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l,r=0,len(arr)-k
        
        while(l<r):
            mid=(l+r)//2
            if (arr[mid]+arr[mid+k])/2<x:#中间值小于x，说明l可以向右移动，直觉是对的
                l=mid+1
            else:# 等于时就r一直往左移就行
                r=mid
            
        return arr[l:l+k]
                
            
                
        
