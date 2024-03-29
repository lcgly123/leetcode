15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]



class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # dfs会重复
        
        nums.sort()
        target=0
        res=[]
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:# 防止重复
                continue
            l,r=i+1,len(nums)-1
            while(l<r):
                s=nums[i]+nums[l]+nums[r]
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    l+=1# 防止重复
                    while(l<r and nums[r]==nums[r-1]):
                        r-=1
                    r-=1
        return res
