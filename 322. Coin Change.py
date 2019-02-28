322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=[float('inf')]*(amount+1)
        res[0]=0
        
     
        
        for i in range(1,amount+1):
            for c in coins:
                if i>=c:
                    res[i]=min(res[i],res[i-c]+1)# 就是如果这个钱-c是可以凑出来的，那这个也可以，如果不可以，那它也可以
                
        if res[amount]==float('inf'):
            return -1
        else:
            return res[amount]
        
        
        
        
        
        
        # 可以但会超时
        
#         def dfs(candidates,target,path,res):
#             if path!=[]:
#                 if sum(path)==target:
#                     return res.append(len(path))
#                 if sum(path)>target:
#                     return 
                
#             for i in range(len(candidates)):
#                 dfs(candidates,target,path+[candidates[i]],res)
   
#         res=[]
#         dfs(coins,amount,[],res)
#         if amount==0:
#             return 0
#         if res!=[]:
#             return min(res)
#         else:
#             return -1

# # 可以但会内存超出限制
#         def bfs(queen,target):
#             queen=queen
#             path=[[x] for x in queen]
            
#             while(queen):
#                 new_layer=[]
#                 new_path=[]
                
                 
                
#                 for i in range(len(queen)):
#                     if sum(path[i])==target:
#                         return len(path[i])
#                     if sum(path[i])>target:
#                         continue
                    
#                     for node in queen:
#                         new_layer.append(node)
#                         new_path.append(path[i]+[node])
                
#                 queen=new_layer
#                 path=new_path
                
#         if amount==0:
#             return 0
#         res=bfs(coins,amount)
#         if res!=None:
#             return res
#         else:
#             return -1
                
                    
                    
            
