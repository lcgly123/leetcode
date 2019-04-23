673. Number of Longest Increasing Subsequence

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        
        if nums==[]:
            return 0
        dp=[1]*len(nums)# 代表最长列的长度
        count=[1]*len(nums)# 代表最长列出现的次数
        
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    if dp[j]+1==dp[i]:# 表明两个j都是最长列，所以最长列出现的次数为他们出现次数的和
                        count[i]+=count[j]
                    elif dp[j]+1>dp[i]:
                        count[i]=count[j]
                    dp[i]=max(dp[i],dp[j]+1)

                    
        maxlen=max(dp)
        return sum([x for i,x in enumerate(count) if dp[i]==maxlen])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
