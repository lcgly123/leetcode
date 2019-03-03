357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 10
        if n==2:
            return 91
        res=[91]
        for k in range(3,n+1):# 3位数有多少个unique数，4位数有多少个unique数
            temp=9*9
            for i in range(k-2):# 就是排列组合，第一位有9个选择，第二位也是9个，接下来才递减
                temp*=(8-i)
            res.append(temp)
            
        return sum(res)
