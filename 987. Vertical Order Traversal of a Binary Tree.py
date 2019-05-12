987. Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic=collections.defaultdict(list)
        queen=[(root,0,0)]
        # 原点节点坐标为（0，0），每下一层行坐标减1，往左，列坐标减1，往右，列坐标加1（原点左右有相同的列坐标）
        # 结果是把所有的节点，从左到右列坐标相同的列整合成一个list，再整到一个list，
        # 每一列内，先按行坐标从从上到下，再按val从小到大排序
        # 好恶心的题目
        
        while(queen):
            new=[]
            for node,row_i,col_i in queen:
                dic[col_i].append((node.val,row_i))
                if node.left:
                    new.append((node.left,row_i-1,col_i-1))
                if node.right:
                    new.append((node.right,row_i-1,col_i+1))
            queen=new
        
        res=[]
        for col in sorted(dic.keys()):
            nodes=[x[0] for x in sorted(dic[col],key=lambda i:(-i[-1],i[0]))]
            res.append(nodes)
        
        return res
            
