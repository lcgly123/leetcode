467. Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        
        dic=collections.defaultdict(int)
        if p=='':
            return 0
        dic[p[0]]=1# 代表有多少种以p[i]结尾的字符子串，因为题目意思：同一个连续子串出现在不同位置算一个，求的是多少种不同的连续子串，所以要加max
        l=0
        for r in range(1,len(p)):
            if ord(p[r])-ord(p[r-1])==1 or p[r-1:r+1]=='za':
                dic[p[r]]=max(dic[p[r]],r-l+1)# 增加这一位增加的连续子串数
            else:
                dic[p[r]]=max(dic[p[r]],1)
                l=r
        # print(dic)
        return sum(dic.values())
        
                    
        

