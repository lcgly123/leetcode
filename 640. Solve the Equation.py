640. Solve the Equation

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"



# 其实挺简单
class Solution:
    def solveEquation(self, equation: str) -> str:
        eq=equation.replace('-',"+-")
        
        left,right=eq.split('=')
        left=left.split('+')
        right=right.split('+')
        
        left_n,left_x=0,0
        for term in left:
            if term.endswith('x'):
                if term=='x':
                    left_x+=1
                elif term=='-x':
                    left_x+=-1
                else:
                    left_x+=int(term[:-1]) 
            else:
                left_n+=int(term) if term!='' else 0
        
        right_n,right_x=0,0
        for term in right:
            if term.endswith('x'):
                if term=='x':
                    right_x+=1
                elif term=='-x':
                    right_x+=-1
                else:
                    right_x+=int(term[:-1]) 
            else:
                right_n+=int(term) if term!='' else 0
                
        # print(left_x,left_n)
        # print(right_x,right_n)
        n=right_n-left_n
        x=left_x-right_x
        
        
        if x==0 and n==0:
            return 'Infinite solutions'
        if x==0 and n!=0:
            return 'No solution'
        
        return 'x={}'.format(n//x)
        
