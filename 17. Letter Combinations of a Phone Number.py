17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].



class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        dic={'2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
            }
        res=[]
        for i,n in enumerate(digits):
            new_res=[]
            if i==0:
                new_res=[x for x in dic[n]]
            else:
                for s in  res:# 生成方式就是之前的，每一个都加上这一位所有的可能
                    for c in dic[n]:
                        new_res.append(s+c)
            res=new_res
        
        return res

