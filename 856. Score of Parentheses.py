856. Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack,cur=[],0
        
        # 实际计算顺序是AB=B+A
        # NB
        for c in S:
            if c=='(':
                stack.append(cur)
                cur=0
            else:
                cur+=stack.pop()+max(cur,1)# 2 * A==A+A
        return cur
        
        


