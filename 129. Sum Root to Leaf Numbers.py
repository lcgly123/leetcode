129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        
        def dfs(root,path,res):
            if root.left==None and root.right==None:
                res.append(int(path))
                return
            if root.left!=None and root.right!=None:
                dfs(root.left,path+str(root.left.val),res)
                dfs(root.right,path+str(root.right.val),res)
            elif root.left!=None:
                dfs(root.left,path+str(root.left.val),res)
            elif root.right!=None:
                dfs(root.right,path+str(root.right.val),res)
        
        if root==None:
            return 0
        res=[]
        path=str(root.val)
        dfs(root,path,res)
        return sum(res)
            
        
