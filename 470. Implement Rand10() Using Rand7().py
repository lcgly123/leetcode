470. Implement Rand10() Using Rand7()

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        def rand5():# NB
            while True:
                i=rand7()
                if i<6:
                    return i
                
        
        while True:
            base=rand7()
            if base>6:
                continue
            if base%2==0:# 奇数对应奇数
                return 2*rand5()
            else:# 偶数对应偶数
                return 2*rand5()-1
