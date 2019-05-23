47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(can,path,res):
            if len(can)==0:
                res.append(path)
                return
            
            for i,n in enumerate(can):
                if i>0 and can[i]==can[i-1]:
                    continue
                can_in=can[:]
                can_in.pop(i)
                dfs(can_in,path+[n],res)
        res=[]
        dfs(sorted(nums),[],res)
        return res
#         # 这种更好，改变搜索队列而不是改指针，更容易理解
#         def dfs(candidates,path,result):
#             if len(candidates)==0:
#                 result.append(path) 
#                 return

#             for i in range(0,len(candidates)):
#                 if (i-1)>=0 and  candidates[i]==candidates[i-1]:
#                     continue  
#                 candidates_in=candidates[:]
#                 candidates_in.pop(i)
#                 dfs(sorted(candidates_in),path+[candidates[i]],result)
        
#         result=[]
#         dfs(sorted(nums),[],result)
        
#         return result
        
        
        
