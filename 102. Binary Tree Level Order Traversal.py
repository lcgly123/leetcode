102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        queen=[root]
        res=[]
        
        while(queen):
            new=[]#下一层节点
            val=[]# 这一层节点的值
            
            for node in queen:
                val.append(node.val)
                new.append(node.left)
                new.append(node.right)
            new=[x for x in new if x]
            res.append(val)
            queen=new
        return res
        
        
        
        
        
        
#         if not root:
#             return []
#         res=[]
#         travel=[root]
#         while(travel):
#             temp=[]
#             temp_val=[]
#             for node in travel:
#                 temp_val.append(node.val)
#                 temp.extend(i for i in [node.left,node.right] if i)
#             res.append(temp_val)
#             travel=temp
        
#         return res
        
        
        
