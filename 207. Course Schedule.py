207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
             
             
             
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        
        
            
        def dfs(candidates):
            # if candidates==[]:
            #     return True
            if visited[candidates]==-1:
                return False
            
            
            visited[candidates]=-1
            for i in gragh[candidates]:
                res=dfs(i)
                if not res:
                    return False
            visited[candidates]=0
            return True
        
        
        
        gragh=[[] for _ in range(numCourses)]
        visited=[0 for _ in range(numCourses)]
        # 有用，用来构造图
        for x,y in prerequisites:
            gragh[x].append(y)
            
        
        for i in range(numCourses):
            res=dfs(i)
            if not res:
                return False
        return True
