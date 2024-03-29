399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        gragh=collections.defaultdict(dict)
        for i,(k,v) in enumerate(equations):
            gragh[k][v]=values[i]
            gragh[v][k]=1/values[i]
            
        def dfs(node,pre,target,seen):
            if node==target:
                return pre
            if node in seen:
                return -1
            
            for next_node in gragh[node]:
                res= dfs(next_node,pre*gragh[node][next_node],target,seen+[node])
                if res!=-1:
                    return res
            return -1
        
        res=[]
        for k,v in queries:
            if k not in gragh or v not in gragh:
                res.append(-1)
            else:
                res.append(dfs(k,1,v,[]))
        
        return res


#         # 我真NB
#         from collections import defaultdict
#         gragh=defaultdict(list)
        
#         for i,(x,y) in enumerate(equations):
#             gragh[x].append([y,values[i]])
#             gragh[y].append([x,1/values[i]])
        
#         # print(gragh)
#         def bfs(root):
#             if root[0] not in gragh or root[1] not in gragh:
#                 return -1
#             queen=[root[0]]
#             path=[[]]
#             visited=defaultdict(int)
            
            
#             while(queen):
#                 print(queen)
#                 new_queen=[]
#                 new_path=[]

#                 for i,node in enumerate(queen):
#                     for subnode in gragh[node]:
#                         if visited[subnode[0]]!=0:
#                             continue
#                         else:
#                             new_queen.append(subnode[0])
#                             new_path.append(path[i]+[subnode[1]])
#                             visited[subnode[0]]=1

#                             if subnode[0]==root[1]:
#                                 return new_path[-1][:]
#                 queen=new_queen
#                 path=new_path
                
#             return -1
                
#         res=[]
#         for root in queries:
#             if bfs(root)==-1:
#                 res.append(-1)
#             else:
#                 temp=1
#                 for i in bfs(root):
#                     temp*=i
#                 res.append(temp)
#         return res
                
                        
                    
                    
                    
                
                        
                    
                    
                    
                    
                    
                    
            
                
        
        
        
        
        

