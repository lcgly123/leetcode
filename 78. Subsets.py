78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        已知一个集合【1,2,3，。。。n】的所有子集，
        则【1,2,3，。。。n，n+1】的所有子集就是原所有子集，并，新元素n+1与原所有子集分别并
        
        '''
        res=[[]]# 首先要有一个空集
        for n in nums:
            res+=[x+[n] for x in res]+[]# 从数学上，应该是生成所有子集的一种方式
        return res
        
        
