763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 题目要求把字符串分开，每一个子串的字符都出现在这个子串，求最少的分割
        dic={}
        for i,c in enumerate(S):
            dic[c]=i
        
        res=[]
        l,r=0,0
        for i,c in enumerate(S):
            r=max(r,dic[c])# 像是dp，看看每一个点最远弹到哪，NB
            if i==r:
                res.append(r-l+1)
                l=r+1
        return res
