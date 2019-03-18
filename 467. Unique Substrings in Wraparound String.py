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
        
        from collections import defaultdict
        count=defaultdict(int)
        
        
        if p=='':
            return 0
        # NB
        start=0
        count[p[0]]=1# 代表有多少种以p[i]结尾的字符子串
        # 假如数完一段后，下一段有四种情况：不相交，在前一段里面，头（1）尾（2）相交（需要更新count[p[i]]），尾（1）头（2）相交(出来的部分才要 更新)，max就是应对后两种情况
        for i in range(1,len(p)):
            if ord(p[i])==ord(p[i-1])+1 or p[i-1:i+1]=='za':
                count[p[i]]=max(count[p[i]],i-start+1)# i-start+1不是连续子串中以p[i]结尾（最多以start开始）的有这么多个，有用
            else:
                start=i
                count[p[i]]=max(count[p[i]],1)
                
        return sum(count.values())
                    
        

