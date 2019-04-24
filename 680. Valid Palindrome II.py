680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.



class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        s=list(s)
        l=0
        r=len(s)-1
        while(l<r):
            if s[l]==s[r]:# 找到不相等的，NB
                l+=1
                r-=1
            else:
                break
        
        s1=s[:]
        s2=s[:]
        s1.pop(l)
        s2.pop(r)
        r1=s1[::-1]
        r2=s2[::-1]
        return s1==r1 or s2==r2
            
        
        
        
        
        





