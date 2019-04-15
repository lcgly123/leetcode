583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".


# 求编辑距离，可以先求最大共同子串
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j],dp[i][j]+(word1[i]==word2[j]))# NB
        
        return len(word1)+len(word2)-2*dp[-1][-1]

