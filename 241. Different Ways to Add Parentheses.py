241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

class Solution:
    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        ops={'+':lambda x,y:x+y,
            '-':lambda x,y:x-y,
            '*':lambda x,y:x*y}
        
        # NB，有点类似二叉树
        def dfs(s):
            res=[]
            try:
                val=int(s)
                return [val]
            except:
                for i,n in enumerate(s):
                    if s[i] in '+-*':
                        left=dfs(s[:i])
                        right=dfs(s[i+1:])
                        res+=[ops[s[i]](l,r) for l in left for r in right]# 代表这一种分割可以产生第三种结果
                return res# 输出结果可以看做深拷贝
        res=dfs(input)
        return res
