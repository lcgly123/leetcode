567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=[ord(x)-ord('a') for x in s1]
        s2=[ord(x)-ord('a') for x in s2]
        
        f1=[0]*26
        f2=[0]*26
        for i in s1:
            f1[i]+=1
        
        # 滑窗，有用，NB
        windowlen=len(s1)
        for i,c in enumerate(s2):
            f2[c]+=1
            if i>=windowlen:
                f2[s2[i-windowlen]]-=1# 注意这里
            if f1==f2:
                return True
            
        return False
            
        
