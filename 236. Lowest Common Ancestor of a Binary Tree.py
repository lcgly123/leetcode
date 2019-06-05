236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def dfs(root,target,path,res):
            if root==None:
                return
            if path[-1]==target:
                res+=path
                return
                
            dfs(root.left,target,path+[root.left],res)
            if res!=[]:
                return
            dfs(root.right,target,path+[root.right],res)
            
        res_p=[]
        dfs(root,p,[root],res_p)
        res_q=[]
        dfs(root,q,[root],res_q)
        
        # print(res_p)
        # print(res_q)
        m=len(res_p)
        n=len(res_q)
        for i in range(min(m,n)):
            if res_p[i].val!=res_q[i].val:
                return res_p[i-1]
        return res_p[-1] if m<n else res_q[-1]
        
        
        
