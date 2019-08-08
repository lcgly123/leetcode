486. Predict the Winner

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
#         dp=[[0]*len(nums) for _ in range(len(nums))]
#         for i in range(len(nums)):
#             dp[i][i]=nums[i]
        
#         for s in range(len(nums)-2,-1,-1):
#             for e in range(s+1,len(nums)):
#                 chooseleft=nums[s]-dp[s+1][e]
#                 chooseright=nums[e]-dp[s][e-1]
#                 dp[s][e]=max(chooseleft,chooseright)
        
#         return dp[0][-1]>=0

        
        def dfs(nums,i,j):
            if i>j:
                return 0
            if i==j:
                return nums[i]
            if (i,j) in memo:
                return memo[(i,j)]
            
            score=max(nums[i]+min(dfs(nums,i+2,j),dfs(nums,i+1,j-1)),
                     nums[j]+min(dfs(nums,i,j-2),dfs(nums,i+1,j-1)))
            memo[(i,j)]=score
            return score
        memo={}
        s=dfs(nums,0,len(nums)-1)
        return s>=sum(nums)-s
        

#         from collections import defaultdict
#         memo=defaultdict(lambda :-1)# memo只是为了遇到搜过的是快速返回，没别的用，只是为了防止超时
#         # 很有意思，但并不难
#         def dfs(nums,i,j,memo):
#             if i>j:
#                 return 0 # 也可以
#             if i==j:
#                 return nums[i]
#             if memo[(i,j)]!=-1:
#                 return memo[(i,j)]
     
            
#             score=max(nums[i]+min(dfs(nums,i+2,j,memo),dfs(nums,i+1,j-1,memo)),# dfs（）代表搜索i-j时（先拿）最多得分，min是因为第二个拿的一定拿最大的，所以下一次只会是两者最小的
#                      nums[j]+min(dfs(nums,i,j-2,memo),dfs(nums,i+1,j-1,memo)))
#             memo[(i,j)]=score
#             return memo[(i,j)]
        
#         total=sum(nums)
#         score=dfs(nums,0,len(nums)-1,memo)
#         print(score)
        
#         return score>=total-score
            
        
        
        
        
        
        
        
