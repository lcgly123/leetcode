318. Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".



# 字符串的比较可以考虑用bit操作
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordbit=[0]*len(words)
        for i in range(len(words)):
            for c in words[i]:
                wordbit[i]|=1<<(ord(c)-ord('a'))# 意思是1左移多少位，前面是移动的数，后面是移动的位数
                
        res=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if wordbit[i]&wordbit[j]==0:
                    res=max(res,len(words[i]*len(words[j])))
                    
        return res
