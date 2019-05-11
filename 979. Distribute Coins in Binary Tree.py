979. Distribute Coins in Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        
        # 将他们搞平衡需要多少移动步数？答案是左右子树需要的金币数的绝对种子和。
        # 这个怎么理解？其实就是需要把子树多的金币挪给根节点，
        # 然后再从根节点分配给另一个缺少金币的子树对应的金币
        # 其实就是规律
        
        global res
        def dfs(root):
            global res
            if root==None:
                return 0
            l_num=dfs(root.left)
            r_num=dfs(root.right)
            res+=abs(l_num)+abs(r_num)
            return root.val+l_num+r_num-1# 返回的是这个root整个树需要移出或者移入的个数
        res=0
        dfs(root)
        return res

 
