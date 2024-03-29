322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        # 组合
        for c in coins:
            for i in range(1,amount+1):
                if i-c>=0:
                    dp[i]=min(dp[i],dp[i-c]+1)
        
        return dp[-1] if dp[-1]!=float('inf') else -1
        
        
        
        # 排列
#         res=[float('inf')]*(amount+1)
#         res[0]=0
        
     
        
#         for i in range(1,amount+1):
#             for c in coins:
#                 if i>=c:
#                     res[i]=min(res[i],res[i-c]+1)# 就是如果这个钱-c是可以凑出来的，那这个也可以，如果不可以，那它也可以
                
#         if res[amount]==float('inf'):
#             return -1
#         else:
#             return res[amount]
        
        
        
