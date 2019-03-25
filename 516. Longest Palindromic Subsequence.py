516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #NB
        def dfs(s,i,j,dp):
            if i>j:
                return 0
            if i==j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]# 就是为了防止重复走
            else:
                if s[i]==s[j]:
                    dp[i][j]=2+dfs(s,i+1,j-1,dp)
                    return dp[i][j]
                else:
                    dp[i][j]= max(dfs(s,i+1,j,dp),dfs(s,i,j-1,dp))
                    return dp[i][j]
            
        dp=[[-1]*len(s) for _ in range(len(s))]
        res=dfs(s,0,len(s)-1,dp)
        return res
        
        
        # 可以但会超时
        # def dfs(s,i,j,dp):
        #     if i>j:
        #         return 0
        #     if i==j:
        #         # dp[i][j]=1
        #         return 1
        #     if s[i]==s[j]:
        #         # 2+dfs(s,i+1,j-1,dp)
        #         return 2+dfs(s,i+1,j-1,dp)
        #     else:
        #         return max(dfs(s,i+1,j,dp),dfs(s,i,j-1,dp))
        # dp=[[1]*(len(s)-1) for _ in range(len(s))]
        # res=dfs(s,0,len(s)-1,dp)
        # return res







