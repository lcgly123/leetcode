365. Water and Jug Problem

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # 这道题的意思是只有x，y，量出z
        from fractions import gcd
        # def gcd(x,y):# 求最大公约数,会就行
        #     if x<y:
        #         temp=x
        #         x=y
        #         y=temp
        #     if y==0:
        #         return 0
        #     if x%y==0:
        #         return y
        #     while(x%y!=0):
        #         m=max(x-y,y)
        #         n=min(x-y,y)
        #         x=m
        #         y=n
        #         if y==0:
        #             return 0
        #     return y
        
        if z==0:
            return True
        d=gcd(x,y)
        print(d)
        if d==0:# 隐含条件z！=0
            return False
        return z%d==0 and x+y>=z
