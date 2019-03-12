450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        
        def dfs(root,key):
            if root==None:
                return
            if key<root.val:
                root.left=dfs(root.left,key)
            elif key>root.val:
                root.right=dfs(root.right,key)
                
            else:
                if root.right==None: # 这里其实左右都行
                    return  root.left
                
                temp=root.right
                while(temp.left!=None):
                    temp=temp.left
                root.val=temp.val
                root.right=dfs(root.right,root.val)#NB
            return root
        return dfs(root,key)
