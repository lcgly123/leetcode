792. Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def match(s,word):
            i=0
            for c in word:
                i = S.find(c, i) + 1# 说明这个速度快
                if not i: return False
            return True
        # 这个可以，但会超时
        # def match(s,word):
        #     i=0
        #     for c in s:
        #         if c==word[i]:
        #             i+=1
        #             if i==len(word):
        #                 return True
        #     return False
        
        res=0
        for w in words:
            if match(S,w):
                res+=1
        return res
        
        
        
