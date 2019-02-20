210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
Example 1:
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
             
             
             
             
class Solution:
    def findOrder(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        gragh=[[] for i in range(numCourses)]
        pre = [0] * numCourses# 记录每个节点有多少个前驱结点
        # 这样前驱结点，就变成了后继节点
        for x,y in prerequisites:
            pre[x]+=1
            gragh[y].append(x)
            
            
        # 就是学完一层在学下一层
        def bfs(candidates,res):
            queen=candidates
            path=candidates
            
            
            
            while(queen):
                new_layer=[]
                new_path=[]
                
                for i in range(len(queen)):
                    for node in gragh[queen[i]]:
                        pre[node]-=1
                        if pre[node]==0:
                            new_layer.append(node)
                new_path=path+new_layer
                if len(new_path)==numCourses:
                    res.append(new_path)
                
                            
                queen=new_layer                 
                path=new_path
                
        
        res=[]
        can=[x for x in range(numCourses) if pre[x]==0]
        bfs(can,res)
        if res==[]:
            return []
        else:
            return res[0]
        
        
#         # 可以，但会超时
#         gragh=[[] for i in range(numCourses)]
        
        
        
#         for x,y in prerequisites:
#             gragh[x].append(y)

#         candidates=[i for i in range(numCourses)]# 直接=赋不上值
        
#         print(gragh)
#         def dfs(candidates,path,res):
#             if len(candidates)==0:
#                 res.append(path[::-1])
#                 return

#             for i in range(len(candidates)):
#                 candidates_in=candidates[:]
#                 path_in=candidates_in.pop(i)
                
#                 flag=True
#                 for x in gragh[candidates[i]]:
#                     if x not in candidates_in:
#                         flag=False
#                 if flag:
#                     dfs(candidates_in,path+[path_in],res)
            
#         res=[]
#         dfs(candidates,[],res)
#         if res==[]:
#             return res
#         else:
#             return res[0]
