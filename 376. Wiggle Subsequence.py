376. Wiggle Subsequence

A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        flag=[1]*len(nums)# 第一次是上升的
        
        if nums==[]:
            return 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]-nums[j]>0 and flag[j]==1:
                    dp[i]=max(dp[i],dp[j]+1)
                    flag[i]=-1
                if nums[i]-nums[j]<0 and flag[j]==-1:
                    dp[i]=max(dp[i],dp[j]+1)
                    flag[i]=1
        temp=dp[-1]
        flag=[-1]*len(nums)# 第一次是下降的
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]-nums[j]>0 and flag[j]==1:
                    dp[i]=max(dp[i],dp[j]+1)
                    flag[i]=-1
                if nums[i]-nums[j]<0 and flag[j]==-1:
                    dp[i]=max(dp[i],dp[j]+1)
                    flag[i]=1
        return max(temp,dp[-1])
            
        
        


