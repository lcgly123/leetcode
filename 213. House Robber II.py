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
             
             
             
             
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def robber_1(nums):
            pre_max=0# 在前一个位置上，的最大值
            pre_pre_max=0# 在前前一个位置上，的最大值
            for i in nums:
                cur=max(pre_pre_max+i,pre_max)# 在现在位置上，的最大值
                pre_pre_max=pre_max
                pre_max=cur
            return pre_max
        if len(nums)==0:
            return 0
        if len(nums)<3:
            return max(nums)
        return max(robber_1(nums[1:]),robber_1(nums[:-1]))
