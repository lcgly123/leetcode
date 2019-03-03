337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        
        #NB
        def dfs(root):
            if root==None:
                return 0,0
            
            robleft,notrobleft=dfs(root.left)
            robright,notrobright=dfs(root.right)
            rob=root.val+notrobleft+notrobright
            notrob=max(robleft,notrobleft)+max(robright,notrobright)# 并不是一次抢一层
            return rob ,notrob
        return max(dfs(root))
            
