692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import collections
        dic=collections.defaultdict(int)
        for w in words:
            dic[w]+=1
        mid=sorted(dic,key=lambda x:(-dic[x],x))# 传进key的就是dic,key，排出来的也是key，NB

        return mid[:k]
            
        



