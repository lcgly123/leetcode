77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(can,target,path,res):
            if len(path)==target:
                res.append(path)
                return
         
            for i,n in enumerate(can):
                dfs(can[i+1:],target,path+[n],res)
        res=[]
        can=[x for x in range(1,n+1)]
        dfs(can,k,[],res)
        return res
            

        
#         def dfs(candidates,path,res):
#             if len(path)==k:
#                 res.append(path)
#                 return
#             for i in range(len(candidates)):
#                 dfs(candidates[i+1:],path+[candidates[i]],res)
                
#         res=[]
#         candidates=[x for x in range(1,n+1) ]
#         dfs(candidates,[],res)
#         return res
