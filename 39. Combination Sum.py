39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #搜索所有的组合
        def dfs(can,index,target,path,res):
            if sum(path)==target:
                res.append(path)
                return
            elif sum(path)>target:
                return
            for i in range(index,len(can)):
                dfs(can,i,target,path+[can[i]],res)
                
        res=[]
        dfs(candidates,0,target,[],res)
        return res
        # 会搜索到所有的排列
#         def dfs(can,target,path,res):
#             if sum(path)==target:
#                 res.append(path)
#                 return
#             elif sum(path)>target:
#                 return
            
#             for n in can:
#                 dfs(can,target,path+[n],res)
        
#         res=[]
#         dfs(candidates,target,[],res)
#         return res


        
    
    # dfs太好了
#         def dfs(candidates,index,target,path,result):
#             if target<0:
#                 return
#             if target==0:
#                 result.append(path)
#                 return
#             for i in range(index,len(candidates)):
#                 dfs(candidates,i,target-candidates[i],path+[candidates[i]],result)
        
#         result=[]
#         dfs(candidates,0,target,[],result)
        
#         return result
    
    
        
