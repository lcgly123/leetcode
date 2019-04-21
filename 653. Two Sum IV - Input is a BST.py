653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        
        #其实很简单，就是建立每一个节点都加入对应的target
        def dfs(root):
            if root==None:
                return False
            if root.val in targets:
                return True
            targets.append(k-root.val)
            return dfs(root.left) or dfs(root.right)
        
        targets=[]
        
        return dfs(root)
            
            
        

