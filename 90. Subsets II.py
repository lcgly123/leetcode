90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        res=[[]]
        for i in range(len(nums)):
            res+=[subset+[nums[i]] for subset in res]

        # 去重
        dic={}
        for x in res:
            dic[str(x)]=0
        result=[]
        for i in dic.keys():
            result.append(eval(i))# 字符串变list，tuple，表达式，神奇
        return result
