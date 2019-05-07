894. All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        
        # 找出所有的满二叉树（外国定义的满二叉树）
        #NB
        def dfs(N):
            if N==1:
                return [TreeNode(0)]
            res=[]
            for l in range(1,N-1,2):# 子树都只能是奇数
                for left in dfs(l):
                    for right in dfs(N-1-l):
                        root=TreeNode(0)
                        root.left=left
                        root.right=right
                        res.append(root)
            return res
        return dfs(N)
                  
