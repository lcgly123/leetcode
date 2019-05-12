991. Broken Calculator

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

 

Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.




class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
#         X到Y难，但是Y到X容易，因为每一步都是确定的选择

# Y到X就是要么（1）除以2，（2）加1

# 如果Y<X：只能加1，如果Y>X就要分情况讨论

# 1. 如果Y是奇数，必然加1

# 2. 如果Y是偶数，必然除以2得到Y/2，（另外一种操作方式是+1,+1,/2得到Y/2-1，但是比/2,-1用的次数多，所以必然是先要/2）

        res=0
        while(X<Y):
            if Y%2==1:
                Y+=1
            else:
                Y/=2
            res+=1
        res+=X-Y
        return int(res)
