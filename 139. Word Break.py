139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res=[0]*(len(s)+1)
        res[0]=1
        
        for i in range(len(s)):
            for w in wordDict:
                if res[i]==1 and s[i:i+len(w)]==w and i+len(w)<=len(s):
                    res[i+len(w)]=1
            
        if res[-1]:
            return True
        else:
            return False
        
        
        
