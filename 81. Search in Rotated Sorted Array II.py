81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l,r=0,len(nums)-1
        
        while(l<=r):
            mid=(l+r)//2
            
            # 去掉重复的
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # # 去掉重复的
            while r > mid and nums[r] == nums[mid]: # tricky part
                r -= 1
            
            if nums[mid]==target:
                return True 
            if nums[l]> nums[mid]:
                if target>=nums[l] or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]>nums[r]:
                if target>nums[mid] or target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1 
            else:
                if target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
                
        return False
        
        
        
        
