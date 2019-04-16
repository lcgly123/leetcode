592. Fraction Addition and Subtraction

Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"


class Solution:
    def fractionAddition(self, expression: str) -> str:
        import math
        # 其实解释分数运算的过程
        exp=expression.replace('+',' +').replace('-',' -')
        frac=[x.split('/') for x in exp.split()]
        
        all_deno=1
        for n,d in frac:# 求总的分母
            all_deno*=int(d)
        
        neme=0
        for n,d in frac:# 求总的分子
            neme+=int(n)*(all_deno//int(d))
        
        factor=math.gcd(neme,all_deno)# 求最大公约数，约分
        return '{}/{}'.format(neme//factor,all_deno//factor)
        
