958. Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1}
and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        # NB
        count=1 if root else 0# 记录非空节点的个数
        queen=[root]
        while(queen):
            x=queen.pop(0)
            if x==None:
                return count==0
            count-=1
            queen+=[x.left,x.right]
            count=count+1 if x.left!=None else count
            count=count+1 if x.right!=None else count
            
                        

                
