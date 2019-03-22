494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        total=sum(nums)+S
        if total%2!=0 or S>sum(nums):
            return 0
        n=total//2
        
        dp=[0]*(n+1)
        dp[0]=1
        for num in nums:
            for i in range(n,num-1,-1):
                dp[i]+=dp[i-num]# 其实还是有几种方式上台阶
        
        return dp[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        


