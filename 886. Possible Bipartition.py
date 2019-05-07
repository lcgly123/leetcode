886. Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        import collections
        
        gragh=collections.defaultdict(list)
        
        for u,v in dislikes:
            gragh[u].append(v)
            gragh[v].append(u)
            
            
        
        def dfs(node,color):
            if node in colors:
                return colors[node]==color
    
            
            colors[node]=color
            for next_node in gragh[node]:
                if not dfs(next_node,1-color):
                    return False
            return True
        
        colors={}
        for node in gragh:
            if node not in colors:
                if not dfs(node,0):
                    return False
        return True
            
            




