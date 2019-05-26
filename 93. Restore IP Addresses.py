93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        def dfs(can,path,res):
            if len(path)==4 and len(can)==0:
                res.append('.'.join(path))
                return
            if len(path)==4 or len(can)==0:
                return
            
            for i in range(1,4):
                if len(can[:i])!=i:# 因为最后一步切片不论剩下几个都可以切n个，以至于重复
                    continue
                if can[:i].startswith('0') and i>1:
                    continue
                if int(can[:i])<=255:
                    dfs(can[i:],path+[can[:i]],res)
                    
        res=[]
        dfs(s,[],res)
        return res
        

        
#         def dfs(candidates,path,res):
#             if len(path)==4 and len(candidates)==0:
#                 print(path,)
#                 res.append('.'.join(path))
#                 return
#             if len(candidates)==0 or len(path)>4:
#                 return
            
#             for i in range(1,4):
#                 if len(candidates[:i])!=i:# 因为最后一步切片不论剩下几个都可以切n个，以至于重复
#                     continue
#                 if candidates[:i].startswith('0') and len(candidates[:i])>1:
#                     continue
#                 if int(candidates[:i])<=255:
#                     dfs(candidates[i:],path+[candidates[:i]],res) #append无返回值
                    
#         res=[]
#         path=[]
#         dfs(s,path,res)

#         return res
                
