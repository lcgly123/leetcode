652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        # 如果左边是0,0，右边是0,0，这样就分不出这两种树，会误认为重复
        # def dfs(root):
        #     if root==None:
        #         return None
        #     tree=[]
        #     tree.append(root.val)
        #     left=dfs(root.left)
        #     right=dfs(root.right)
        #     if left!=None:
        #         tree+=left
        #     if right!=None:
        #         tree+=right
        #     dic[tuple(tree)]+=1
        #     return tree
        
        def dfs(root):
            if root==None:
                return '#'
            tree=str(root.val)+dfs(root.left)+dfs(root.right)
            if tree in dic and dic[tree]==1:# 只加一次
                res.append(root)
            dic[tree]+=1
            return tree
        
        
        
        import collections
        dic=collections.defaultdict(int)
        res=[]# 这样更好，NB
        _=dfs(root)
        return res
        
        





















