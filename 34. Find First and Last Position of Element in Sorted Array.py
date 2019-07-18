34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


class Solution:
    def searchRange(self, nums, target):
        l,r=0,len(nums)-1
        while(l<=r):
            mid=(l+r)//2
            
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                s,e=mid,mid
                while(s>0 and nums[s]==nums[s-1]):
                    s-=1
                while(e<len(nums)-1 and nums[e]==nums[e+1]):
                    e+=1
                return [s,e]
        return [-1,-1]
        
    
    
#         # 双指针
#         start,end=-1,-1
#         l,r=0,len(nums)-1
#         while(l<=r):
#             if nums[l]==target:
#                 start=l
#             else:
#                 l+=1
#             if nums[r]==target:
#                 end=r
#             else:
#                 r-=1
            
#             if start!=-1 and end!=-1:
#                 break
#         return [start,end]
        
        
        
        
        
