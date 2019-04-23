662. Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 
      
      


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        # 不能直接数坐标，因为可能那一层只有他一个
        def dfs(root,level,index,start):
            global res
            if root==None:
                return
            if len(start)==level:# 只在第一次进入的时候加,NB
                start.append(index)
            res=max(res,index-start[level]+1)
            dfs(root.left,level+1,index*2,start)
            dfs(root.right,level+1,index*2+1,start)
            
        global res
        res=0
        dfs(root,0,0,[])
        return res
            
        
