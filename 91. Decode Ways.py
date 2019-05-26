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
        dp[1] = 1 if 0 < int(s[0]) <= 9 else 0# 虽然在这个里是多余的，但是一般要判断这一位符合什么条件，再确定相应的值
        
        for i in range(2,len(s)+1):
            if 0<int(s[i-1:i])<=9:
                dp[i]+=dp[i-1]
            if s[i-2:i][0] != '0' and 0<int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
                
        return dp[-1]
            
