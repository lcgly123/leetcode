372. Super Pow

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        value=0
        for i in b:
            value=value*10+i
            
        # return pow(a,value)%1337
        return pow(a,value,1337)# 虽然意思和上面的一样，但上面的会超时，而内置pow不会
