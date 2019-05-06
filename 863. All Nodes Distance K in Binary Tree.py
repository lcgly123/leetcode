863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        import collections
        gragh=collections.defaultdict(list)
        
        def dfs1(root):
            if root==None:
                return
            if root.left:
                gragh[root.val].append(root.left.val)
                gragh[root.left.val].append(root.val)
                dfs1(root.left)
            if root.right:
                gragh[root.val].append(root.right.val)
                gragh[root.right.val].append(root.val)
                dfs1(root.right)
        
        # 因为是无向图，可以来回跳
        def dfs2(node,k,res):
            if node in seen:
                return 
            if k==K:
                res.append(node)
                return 
            seen.append(node)
            for next_node in gragh[node]:
                dfs2(next_node,k+1,res)
        
        dfs1(root)
        # print(gragh)
        res=[]
        seen=[]
        dfs2(target.val,0,res)
        
        return res
            
            
                

