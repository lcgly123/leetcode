213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
             
             
             
             
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 更好理解
        def rob(nums):
            if len(nums)==2:
                return pre
            
            curmax=0
            pre=max(nums[:2])
            prepre=nums[0]
            for i in range(2,len(nums)):
                curmax=max(pre,prepre+nums[i])
                prepre=pre
                pre=curmax
            return curmax
        
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        else:
            return max(rob(nums[1:]),rob(nums[:-1]))
        


        
        # def robing(nums):
        #     premax=0
        #     prepremax=0
        #     for n in nums:
        #         curmax=max(prepremax+n,premax)
        #         prepremax=premax
        #         premax=curmax
        #     return curmax
        # if nums==[]:
        #     return 0
        # elif len(nums)<3:
        #     return max(nums)
        # else:
        #     return max(robing(nums[1:]),robing(nums[:-1]))
