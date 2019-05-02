814. Binary Tree Pruning

We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        # 题意：减掉所有全零子树
        def dfs(root):
            if root==None:
                return
            root.left=dfs(root.left)
            root.right=dfs(root.right)
            
            if root.val==1:
                return root
            else:
                return None if root.left==None and root.right==None else root
        
        root=dfs(root)
        return root
                    
               
