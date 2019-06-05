207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        gragh=collections.defaultdict(list)
        for k,v in prerequisites:
            gragh[k].append(v)
        
        seen=[0]*numCourses
        def dfs(node):
            if node not in gragh:
                return True
            if seen[node]==1:
                return False
            for next_node in gragh[node]:
                seen[node]=1
                if not dfs(next_node):
                    return False
                seen[node]=0
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        
        
        
        
        # 有指向同一个点，不一定是有向的环（循环）
#         dic={}
#         def get_head(x):
#             if x not in dic:
#                 dic[x]=x
#             if dic[x]!=x:
#                 dic[x]=get_head(dic[x])
#             return dic[x]
        
#         for x,y in prerequisites:
#             head1=get_head(x)
#             head2=get_head(y)
#             if head1==head2:# 有指向同一个点，不一定是有向的环（循环）
#                 return False
#             dic[head1]=head2
#         return True
                
