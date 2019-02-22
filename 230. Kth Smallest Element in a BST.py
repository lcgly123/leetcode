230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 自己想的，答案用全局变量（一个类变量）更好一些
        def dfs(root,count,k):
            if root!=None:
                print(root.val,count)
            if root==None:
                return 
            if root.left==None and root.right==None:
                count+=1
                if count==k:
                    return root.val
                else:
                    return
            
            res=dfs(root.left,count,k)
            if res!=None:
                return res
            else :
                count+=1
                if count==k:
                    return root.val
                else:
                    res=dfs(root.right,count,k)
                    return res
                    
                    
        res=dfs(root,0,k)
        return res

















