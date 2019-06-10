513. Find Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        
        queen=[root]
        while(queen):
            new=[]
            
            for node in queen:
                new+=[x for x in [node.left,node.right] if x!=None]
            
            if new==[]:
                return queen[0].val
            else:
                queen=new
        
        
        
