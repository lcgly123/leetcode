40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """     
        def dfs(can,target,path,res):
            if sum(path)==target:
                res.append(path)
                return
            elif sum(path)>target:
                return
            for i,n in enumerate(can):
                if i>0 and can[i]==can[i-1]:
                    continue
                dfs(can[i+1:],target,path+[can[i]],res)

        res=[]
        dfs(sorted(candidates),target,[],res)
        return res
#         # 这种更好，改变搜索队列而不是改指针，更容易理解
#         def dfs(candidates,target,path,result):
#             if target<0:
#                 return
#             if target==0:
#                 result.append(path) 
#                 return

#             for i in range(0,len(candidates)):
#                 if (i-1)>=0 and  candidates[i]==candidates[i-1]:
#                     continue  
#                 dfs(candidates[i+1:],target-candidates[i],path+[candidates[i]],result)
        
#         result=[]
#         dfs(sorted(candidates),target,[],result)
        
#         return result
