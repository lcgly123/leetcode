858. Mirror Reflection

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # 每一个增殖的箱子都相当于是沿着某条边进行对称翻转。
        # 规律
        
        import math
        
        if p==q:
            return 1
        r=math.gcd(p,q)
        p//=r
        q//=r
        
        # 规律，很好理解，想象增殖一个箱子
        if p%2==1 and q%2==1:
            return 1
        elif p%2==0 and q%2==1:
            return 2
        elif p%2==1 and q%2==0:
            return 0
        
        
        
        





