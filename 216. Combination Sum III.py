216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]




class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        def dfs(can,n,k,path,res):
            if len(path)==k:
                if sum(path)==n:
                    res.append(path)
                return
            for i,c in enumerate(can):
                dfs(can[i+1:],n,k,path+[c],res)
        
        res=[]
        dfs([1,2,3,4,5,6,7,8,9],n,k,[],res)
        return res
