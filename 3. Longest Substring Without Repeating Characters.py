3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index=collections.defaultdict(int)
        l=0
        res=0
        
        # 分类讨论
        for r in range(len(s)):
            if s[r] not in index:
                res=max(res,r-l+1)
            elif s[r] in index and index[s[r]]<l:# index[s[r]]在l前面直接算
                res=max(res,r-l+1)
            elif s[r] in index:
                l=index[s[r]]+1
            index[s[r]]=r
                
        return res
                
                
        
        

        
#         out=None
#         char_dic = {}
#         max_so_far = curr_max =start = 0
        
         

#         for index, char in enumerate(s):
#             if char in char_dic and char_dic[char] >= start:# start就是下一次从start开始
#                 max_so_far = max(max_so_far, curr_max)
#                 curr_max = index - char_dic[char]
#                 start = char_dic[char] + 1

#             else:
#                 curr_max+=1 #这里从start开始的curr_max个开始加
#                 if curr_max>max_so_far:
#                     out=s[index-curr_max]#输出至多是这些，
#                                         # 下一次只会比这个少而不会多，所以这个就是最大子串的输出
 
                
#             char_dic[char]=index
        
        
#         print(out)
#         return max(max_so_far, curr_max)
        
