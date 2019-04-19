623. Add One Row to Tree

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        row=[]
        
        dummy,dummy.left=TreeNode(None),root
        queen=[dummy]
        k=0
        while k<(d-1):
            new_layer=[]
            for new_root in queen:
                if new_root.left!=None:
                    new_layer.append(new_root.left)
                if new_root.right!=None:
                    new_layer.append(new_root.right)
            queen=new_layer
            k+=1
        
        for node in queen:
            node.left,node.left.left=TreeNode(v),node.left
            node.right,node.right.right=TreeNode(v),node.right
            
        return dummy.left
                
            
        


