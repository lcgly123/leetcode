332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.




class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        gragh=collections.defaultdict(list)
        for k,v in tickets:
            gragh[k].append(v)
            gragh[k].sort()
        
        def dfs(node,path,res):
            if len(path)==len(tickets)+1:
                res.append(path)
                return True
            # if len(gragh[node])==0:
            #     return False
            for i,_ in enumerate(gragh[node]):#可以循环但不能重复一张票
                next_node=gragh[node].pop(i)
                if dfs(next_node,path+[next_node],res):
                    return True
                gragh[node].insert(i,next_node)
                
        res=[]
        dfs('JFK',['JFK'],res)
        return res[0] 
        
#         import collections
#         # 没有给节点数的建图方式
#         gragh=collections.defaultdict(list)
#         for i,j in tickets:
#             gragh[i].append(j)
#             gragh[i].sort()

#         path=[]
#         res=[]
#         def dfs(root,path,res):
#             if len(path)==len(tickets)+1:# 这才是终止条件
#                 res.append(path)
#                 return True
#             if gragh[root]==[]:
#                 return False

#             for i in range(len(gragh[root])):
#                 node=gragh[root].pop(i)
#                 out=dfs(node,path+[node],res)
#                 if out:# 只要搜到第一个，不然会超时
#                     return True
#                 gragh[root].insert(i,node)# 一定要把图恢复原状，不然回去是时候图变了，有用
            
#         a=dfs('JFK',path+['JFK'],res)
#         return res[0]
                
            
        
        
            






