508. Most Frequent Subtree Sum

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        
        def dfs(root,dic):# dic有用，其他没啥
            if root==None:
                return 0
            if root.left==None and root.right==None:
                dic[root.val]+=1
                return root.val
            
            left=dfs(root.left,dic)
            right=dfs(root.right,dic)
            total=root.val+left+right
            dic[total]+=1
            return total
        
        if root==None:
            return []
        dic=collections.defaultdict(int)
        dfs(root,dic)
        most=max(dic.values())
        res=[x for x in dic.keys() if dic[x]==most]
        return res
