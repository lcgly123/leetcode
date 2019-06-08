140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        def dfs(can,target):
            if target=='':
                return ['']
            if target in memo:
                return memo[target]
            res=[]
            for i,w in enumerate(can):
                if target.startswith(w):
                    mid_res=dfs(can,target[len(w):])
                    res+=[w+' '+x  if x!=''else w for x in mid_res ]
            memo[target]=res
            return res
                    
        memo=collections.defaultdict(list)
        return dfs(wordDict,s)
