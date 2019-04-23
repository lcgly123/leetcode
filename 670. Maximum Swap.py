670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973


class Solution:
    def maximumSwap(self, num: int) -> int:
        s=list(str(num))
        s_init=s[:]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                s[i],s[j]=s[j],s[i]
                if s>s_init:#NB
                    s_init=s[:]
                s[i],s[j]=s[j],s[i]#要有
                
        return int(''.join(s_init))
            
                
            
            
        
        
        
        
        
        
        
        
        
        
        






