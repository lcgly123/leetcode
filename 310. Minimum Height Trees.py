310. Minimum Height Trees

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]



class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 用这个建立无向图，用于边只给一次
        gragh=[[] for i in range(n)]# 用set保险一些，防止出现重复的边
        for x,y in edges:
            gragh[x].append(y)
            gragh[y].append(x)
        
        
        remains=[i for i in range(len(gragh))]
        leaves=[i for i in remains if len(gragh[i])==1]# 如果边为1就是叶子节点
        
        while(len(remains)>2):            
            for leaf in leaves:
                neighbor=gragh[leaf].pop() # 就是叶子节点唯一的相关节点,之后叶子节点会变成[],有用
                gragh[neighbor].remove(leaf)# 删除相邻节点中的叶子节点
                
                remains.remove(leaf)
            leaves=[i for i in remains if len(gragh[i])==1]
        
        return remains
