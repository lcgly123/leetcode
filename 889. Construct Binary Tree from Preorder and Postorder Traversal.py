889. Construct Binary Tree from Preorder and Postorder Traversal

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        def dfs(pre,post):
            if pre==[]:
                return 
            root=TreeNode(pre[0])
            if len(pre)>1:
                if pre[1]==post[-2]:# 只有一边有
                    root.right=dfs(pre[1:],post[:-1])# 这时候建在哪边都可以root.left=dfs(pre[1:],post[:-1])也对
                else:
                    last_in_post_left=post.index(pre[1])
                    first_in_pre_right=pre.index(post[-2])
                    root.left=dfs(pre[1:first_in_pre_right],post[:last_in_post_left+1])
                    root.right=dfs(pre[first_in_pre_right:],post[last_in_post_left+1:-1])
            return root
            
        return dfs(pre,post)
        
        
        
        









