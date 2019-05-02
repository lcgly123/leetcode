802. Find Eventual Safe States

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # 题意：找所有能到终结节点的节点
        # 找环，看看一个节点是不是在环中
        def dfs(node):
            seen[node]=0
            for next_node in graph[node]:
                if seen[next_node]==0 or (seen[next_node]==-1 and dfs(next_node)):#有用
                    return True
            seen[node]=1# 必须的，1，如果不改就是0了，设想从另一个节点过来，就不会往下走，导致错误2，减少计算量
            res.append(node)
            return False
        
        res=[]
        seen=[-1]*len(graph)
        for node in range(len(graph)):
            if seen[node]==-1:
                dfs(node)
                
        return sorted(res)
                
                
