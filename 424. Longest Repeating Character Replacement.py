424. Longest Repeating Character Replacement

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        count=defaultdict(int)
        start=0
        max_c=0
        
        # 最长滑窗一旦达到就不会缩小，只会一直往后走，除非变的更长
        for end,c in enumerate(s):
            count[c]+=1
            max_c=max(max_c,count[c])# 表示滑窗里曾经最多的字符的个数，直到有新的字符个数超过上一个最大值
            
            if end-start+1-max_c>k:#就是说k个已经填不了了
                count[s[start]]-=1
                start+=1
                
        return len(s)-start
            
        
        
