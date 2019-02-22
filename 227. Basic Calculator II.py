227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops={'+':lambda stack,val:stack.append(val),
            '-':lambda stack,val:stack.append(-val),
            '*':lambda stack,val:stack.append(stack.pop()*val),
            '/':lambda stack,val:stack.append(int(stack.pop()/val)),
            }
        
        stack,val,op=[],0,'+'
        
        for i in s:
            try:
                val=val*10+float(i)
            except:
                if i==' ':
                    pass
                else:
                    ops[op](stack,val)# 这里的符号实际上是上一个符号
                    val=0
                    op=i
        ops[op](stack,val)# 所以还需要一次，这个是最后一个符号
        return int(sum(stack))





















