368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # NB
        nums.sort()
        if nums==[]:
            return []
        dp=[[x] for x in nums]# 意思是nums[i]能整除的最长的序列，未必是最长的
        max_list=[]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[i])<len(dp[j])+1:
                    dp[i]=dp[j]+[nums[i]] # 更新dp[i]
                    
                    if len(dp[i])>len(max_list):
                        max_list=dp[i][:]
            # print(dp)
        
        if max_list==[]:
            return dp[-1]
        else:
            return max_list
                    
