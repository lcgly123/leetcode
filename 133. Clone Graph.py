133. Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # 其实就是复制到dic里，dic的k是原值，v是新值
        def dfs(node):
            if node==None:
                return
            for next_node in node.neighbors:
                if next_node in dic:
                    dic[node].neighbors.append(dic[next_node])
                else:
                    new_node=Node(next_node.val,[])
                    dic[next_node]=new_node
                    dic[node].neighbors.append(dic[next_node])
                    dfs(next_node)
        
        dic={node:Node(node.val,[])}
        dfs(node)
        return dic[node]

#         def dfs(node):
#             # 走到走过的节点还要循环一次，因为是无向图，不需要停止条件，循环完就完
#             for nei in node.neighbors:
#                 if nei in dic:
#                     dic[node].neighbors.append(dic[nei])
#                 else:
#                     dic[nei]=Node(nei.val,[])
#                     dic[node].neighbors.append(dic[nei])
#                     dfs(nei)
        
#         dic={node:Node(node.val,[])}
#         dfs(node)
#         return dic[node]
