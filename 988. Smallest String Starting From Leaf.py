988. Smallest String Starting From Leaf


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # 一个二叉树每个节点上面是个0-25的数字代表了a-z各个数字，
        # 从叶子节点走向根节点的路径可以看做一个字符串，
        # 现在求所有字符串中字典顺序最小的那个是什么。
        def dfs(root,path,res):
            if not root.left and not root.right:
                res.append(chr(root.val+ord('a'))+path)
                return
            cur=chr(root.val+ord('a'))
            if root.left:
                dfs(root.left,cur+path,res)
            if root.right:
                dfs(root.right,cur+path,res)
                
        res=[]
        path=''
        dfs(root,path,res)
        res.sort()
        return res[0]
        
#         # 这个答案：所有有比较的节点（同时具有左右节点）都是正确地，但根节点如果没有比较的话
#         # 就会得到错误的答案,如下：
#        #          z
#        #         /  
#        #        b    
#        #      /   \ 
#        #     a     a
#        #    / 
#        #   b
#        #  /
#        # a
    
#         def dfs(root):
#             if root==None:
#                 return
#             left=dfs(root.left)
#             right= dfs(root.right)
            
#             cur=chr(root.val+ord('a'))
            
#             if not left and not right:
#                 return cur
#             elif left!=None and right==None:
#                 return left+cur
#             elif right!=None and left==None:
#                 return right+cur
#             else:
#                 return min(left+cur,right+cur)
        
#         return dfs(root)
