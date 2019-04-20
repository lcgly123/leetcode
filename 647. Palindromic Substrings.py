647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # 有用，这个好
        def pal_recog(s,l,r):
            count=0
            while(l>=0 and r<len(s)):
                if s[l]==s[r]:
                    count+=1
                    l-=1
                    r+=1
                else:
                    break
            return count
        
        res=0
        for i in range(len(s)):
            res+=pal_recog(s,i,i)
            res+=pal_recog(s,i,i+1)
            
        return res
        
