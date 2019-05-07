890. Find and Replace Pattern

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.



class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def match(word,pattern):
            dic={}
            if len(word)!=len(pattern):
                return False
            for w,p in list(zip(word,pattern)):
                if p in dic and dic[p]!=w:# 两类不匹配
                    return False
                elif p not in dic and w in dic.values():# 两类不匹配
                    return False
                else:
                    dic[p]=w
            return True
        
        res=[]
        for word in words:
            if match(word,pattern):
                res.append(word)
        
        return res
            
                    
