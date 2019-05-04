848. Shifting Letters

We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        # 题意：每一个shifts[i]代表前面所有字母要向右移动的位数
        # NB
        total=sum(shifts)
        
        S=list(S)
        for i,c in enumerate(S):
            S[i]=chr(ord('a')+(ord(c)-ord('a')+total)%26)# 注意字符串是常量，不可更改，所以要用S[i]而不是c，（唉，也不报错）
            total-=shifts[i]
            
        return ''.join(S)
        
        
        

