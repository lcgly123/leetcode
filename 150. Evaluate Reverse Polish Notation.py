150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

        # NB
        ops = {'+':lambda x, y: x+y, '-':lambda x, y: x-y, '*':lambda x, y: x*y, '/':lambda x, y: x/y}
        
        res=[]
        for i in tokens:
            try:
                res.append(float(i))#NB
            except:
                res.append(int(ops[i](res.pop(-2),res.pop(-1))))# 1，pop顺序不能乱，2，不能用//,它是向下取整，遇见负数不对，int向0取整
         
                
        return int(res[-1])
