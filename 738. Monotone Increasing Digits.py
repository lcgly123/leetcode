738. Monotone Increasing Digits

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299




class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        
        def dfs(s):#NB
            if len(s)==1:
                return s
            if s[0]*len(s)<=s:# 测试s【0】和s【1】是升序
                return s[0]+dfs(s[1:])
            else:
                return chr(ord(s[0])-1)+'9'*(len(s)-1)# 不是的话就这样做就行
        
        return int(dfs(str(N)))
        
