394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


class Solution:
    def decodeString(self, s: str) -> str:

        stack=[['',1]]# 这个1其实没啥用
        num=''
        pattern=''
        for c in  s:
            if c in '0123456789':
                num+=c
            elif c=='[':
                stack.append(['',int(num)])
                num=''
            elif c==']':
                cur_pattern,cur_num=stack.pop()
                stack[-1][0]+=cur_pattern*cur_num
            else:
                stack[-1][0]+=c
                
        return stack[-1][0]
                
                
                
        
        
        
        
#         # 想想都觉得自己很NB
#         def dfs(s,i):
#             num=''
#             pattern=''
#             while(i<len(s)):
#                 if s[i] in '0987654321':
#                     num+=s[i]
#                     i+=1
#                 elif s[i]=='[':
#                     pattern_in,i=dfs(s,i+1)
#                     if num=='':
#                         pattern+= pattern_in
#                         num=''# 处理好一个pattren了
#                     else:
#                         pattern+=pattern_in*int(num)
#                         num=''
#                 elif s[i]==']':
#                     if num=='':
#                         return pattern,i+1
#                 else:
#                     pattern+=s[i]
#                     i+=1
                
#             return pattern,i
        
#         res,_=dfs(s,0)
#         return res
            
            
            
            
            
            
