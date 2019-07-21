91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        if not s:
            return 0
    
        dp=[0]*(len(s)+1)
        dp[0]=1
        
        for i in range(len(s)):
            if int(s[i])>0:
                dp[i+1]+=dp[i]
            if i>0 and 0<int(s[i-1:i+1])<=26 and s[i-1]!='0':
                dp[i+1]+=dp[i-1]
        
        return dp[-1]
        
        
        
        
            
