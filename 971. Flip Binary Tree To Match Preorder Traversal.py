971. Flip Binary Tree To Match Preorder Traversal

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

 

Example 1:



Input: root = [1,2], voyage = [2,1]
Output: [-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        # 其实不难
        global i
        i=0
        def dfs(root):
            global i
            if root==None:
                return True
            if root.val!=voyage[i]:#这是反转后的
                return False
            i+=1
            if root.left and root.left.val!=voyage[i]:
                res.append(root.val)# 返回的是母节点的值
                root.left,root.right=root.right,root.left
            return dfs(root.left) and dfs(root.right)
        
        res=[]
        flag=dfs(root)# 代表可以使它俩相同，不论反不反转
        return res if flag else [-1]
            
            
