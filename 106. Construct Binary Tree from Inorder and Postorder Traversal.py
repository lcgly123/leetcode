106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        
        def dfs(inorder,postorder):
            if len(inorder)==0:
                return None

            val=postorder.pop() 
            root=TreeNode(val)
            in_index=inorder.index(val)
            
            # 后序倒放=先序的镜像
            root.right=dfs(inorder[in_index+1:],postorder)
            root.left=dfs(inorder[:in_index],postorder)
            
            return root
        
        res=dfs(inorder,postorder)
        return res
