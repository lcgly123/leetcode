222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        queen=[root]
        res=1
        while(queen):
            new=[]
            for node in queen:
                new+=[x for x in [node.left,node.right] if x is not None]
                
            res+=len(new)
            queen=new
        return res

    
        
        
        
        
        
#         if root==None:
#             return 0
#         queen=[root]
#         count=1
#         while(queen):
#             new_layer=[]
            
#             for node in queen:
#                 if node.left!=None:
#                     new_layer.append(node.left)
#                     count+=1
#                 if node.right!=None:
#                     new_layer.append(node.right)
#                     count+=1
                    
#             queen=new_layer
#         return count
