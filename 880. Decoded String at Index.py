880. Decoded String at Index

An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".



class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        
        N=0
        # 计算一下需要展开到哪
        # NB
        for i,c in enumerate(S):
            if c.isalpha():
                N+=1
            elif c.isdigit():
                N=N*int(c)
            
            if N>=K:
                break
        
        # 想象一个解码后的字符串，一个对应的原字符串，一点点倒回去
        for j in range(i,-1,-1):# 再倒回去
            if S[j].isdigit():
                N/=int(S[j])
                K=K%N# 计算第K个在第一个单位的位置
            else:
                if K==N or K==0:# K==N表示在一个单位内部，K==0表示刚好在一个单位上
                    return S[j]
                N-=1
                
                
            
        
        
        # 可以，但会内存溢出
#         res=''
#         for c in S:
            
#             if c.isalpha():
#                 res+=c
#             elif c.isdigit():
#                 res=res*int(c)
#             if len(res)>=K:
#                 # print(res)
#                 return res[K-1]
        
        
        
        
        
        
