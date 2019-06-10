516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # NB
        
        def dfs(s,i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i]==s[j]:
                res=2+dfs(s,i+1,j-1)
            else:
                res=max(dfs(s,i+1,j),dfs(s,i,j-1))
            memo[(i,j)]=res
            return res
        
        memo={}
        return dfs(s,0,len(s)-1)
        
        
        
        
        
        
        







