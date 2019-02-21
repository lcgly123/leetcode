201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
Example 1:
Input: [5,7]
Output: 4
Example 2:
Input: [0,1]
Output: 0


class Solution:
    def rangeBitwiseAnd(self, m: 'int', n: 'int') -> 'int':
        # 就是一种方法吧，了解
        count=0
        while(n!=m):
            n>>=1
            m>>=1
            count+=1
        return m<<count

