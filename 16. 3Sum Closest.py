16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).



class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cur_min=float('inf')
        res=0
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                s=nums[i]+nums[l]+nums[r]-target# 有用
                if abs(s)<cur_min:
                    cur_min=abs(s)
                    res=nums[i]+nums[l]+nums[r]
                if s<0:
                    l+=1
                else:
                    r-=1
        
        return res
