926. Flip String to Monotone Increasing

A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.


class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        
        zero_num=S.count('0')
        flip_num=zero_num
        meet_zero=0
        for i,c in enumerate(S):
            if c=='0':
                meet_zero+=1
            # 在某一位置，把S变单调，需要把他之前的都变成0，之后的都变成1，反转次数就是他俩之和
            # (i + 1 - zero_num)前面的1的个数，(zero_num - meet_zero)后面的0的个数
            # 其实是每一个位置上都试一次，找最小
            flip_num=min(flip_num,(zero_num - meet_zero) + (i + 1 - meet_zero))
            
        return flip_num
                
        
