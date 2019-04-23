678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True






class Solution:
    def checkValidString(self, s: str) -> bool:
        # NB
        cmin=cmax=0# cmax把*全看作（，cmin相反
        for c in s:
            if c=='(':
                cmin+=1
                cmax+=1
            elif c==')':
                cmax-=1
                cmin=max(0,cmin-1)
            elif c=='*':
                cmax+=1
                cmin=max(0,cmin-1)
            if cmax<0:# 说明即使*全视为（，）也太多了
                return False
        return cmin==0 # cmin》0 说明即使*全视为），（也太多了
                

        


