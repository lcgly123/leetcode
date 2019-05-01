785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.






class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # 二分图，二部图，是指相邻节点都不同的图
        def dfs(node,color):
            if node in dic:
                return dic[node]==color # 看看是否染对
            dic[node]=color
            
            for next_node in graph[node]:
                if dfs(next_node,1-color)==False: # 有一个染错就错
                    return False
            return True
        
        dic={}
        for node in range(len(graph)):
            if node not in dic:# 重新进入的不算
                if dfs(node,1)==False:
                    return False
        
        return True
        
        










