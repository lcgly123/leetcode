343. Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        数字4拆成2+2，乘积最大，为4。

数字5拆成3+2，乘积最大，为6。

数字6拆成3+3，乘积最大，为9。

数字7拆为3+4，乘积最大，为12。

数字8拆为3+3+2，乘积最大，为18。

数字9拆为3+3+3，乘积最大，为27。

数字10拆为3+3+4，乘积最大，为36。

....

那么通过观察上面的规律，我们可以看出从5开始，数字都需要先拆出所有的3，一直拆到剩下一个数为2或者4，因为剩4就不用再拆了
        '''
        if n==2:
            return 1
        elif n==3:
            return 2
        elif n==4:
            return 4
        elif n>4:
            temp=n
            res=1
            while(temp>4):
                res*=3
                temp-=3
            res*=temp
            return res
                
            


