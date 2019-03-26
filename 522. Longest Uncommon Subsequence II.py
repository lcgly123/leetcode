522. Longest Uncommon Subsequence II

Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3



class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_substr(w1,w2):#就是看看w1是不是w2的子串（不一定连续）
            i=0
            for c in w2:
                if i<len(w1) and w1[i]==c:
                    i+=1
            return i==len(w1)
        
        strs.sort(key=len,reverse=True)
        
        for w1 in strs:
            mid_res=[ is_substr(w1,w2) for w2 in strs if len(w1)<=len(w2)]
            if sum(mid_res)-1==0:# sum（【】）==0
                return len(w1)# 对，因为排过序，下一个不可能是上一个的子串
                
        return -1








