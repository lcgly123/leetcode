46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(can,path,res):
            if len(can)==0:
                res.append(path)
                return
            
            for i,n in enumerate(can):
                can_in=can[:]
                can_in.pop(i)
                dfs(can_in,path+[n],res)
        res=[]
        dfs(nums,[],res)
        return res
        
        
        
#         # 这种更好，改变搜索队列而不是改指针，更容易理解
#         def dfs(candidates,path,result):
#             if len(candidates)==0:
#                 result.append(path) 
#                 return

#             for i in range(0,len(candidates)):
#                 candidates_in=candidates[:]
#                 candidates_in.pop(i)
#                 dfs(candidates_in,path+[candidates[i]],result)
        
#         result=[]
#         dfs(sorted(nums),[],result)
        
#         return result
        
        
        
        
