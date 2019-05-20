5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
 
        
        res=''
        max_len=0
        for i in range(len(s)):
            
            l,r=i,i
            while(l>=0 and r<len(s)):
                if s[l]==s[r]:
                    if max_len<r-l+1:
                        max_len=r-l+1
                        res=s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
            
            l,r=i,i+1
            while(l>=0 and r<len(s)):
                if s[l]==s[r]:
                    if max_len<r-l+1:
                        max_len=r-l+1
                        res=s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
        
        return res
            
        
        
        
        
        
        
