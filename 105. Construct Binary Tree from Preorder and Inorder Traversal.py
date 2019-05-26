105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        
        def dfs(inorder,preorder):
            if len(inorder)==0:
                return None

            val=preorder.pop(0)
            root=TreeNode(val)
            in_index=inorder.index(val)
            root.left=dfs(inorder[:in_index],preorder)# 先把这个跑完再跑下面的，preorder一直在变
            root.right=dfs(inorder[in_index+1:],preorder)
            return root
        
        res=dfs(inorder,preorder)
        return res
            
            
        
        
        
