712. Minimum ASCII Delete Sum for Two Strings

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]#代表在i，j除的最大公共子串
        
        
        # 找最大公共子串
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i]==s2[j]:
                    dp[i+1][j+1]=dp[i][j]+ord(s1[i])
                else :
                    dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
                    
        res=sum(map(ord,s1+s2))-2*dp[-1][-1]
        return res
        
        









