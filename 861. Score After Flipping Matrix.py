861. Score After Flipping Matrix

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39



class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        
        
        # 算法：每一行的第一个数字代表二进制的最高位，因此，首先需要翻转行，以使该位为 1。
        # 每一列的 1 的权重（即转换为二进制后的值）是一致的，因此为了使得和最大，
        # 我们需要翻转列，使得每一列的 1 的个数大于 0 的个数。
        
        # 我也是NB，比答案更好
        mid=[[1-x if row[0]==0 else x for x in row ] for row in A ]# if else在for之前，有用
        mid=list(zip(*mid))
        mid=[[1-x if row.count(0)>len(row)/2 else x for x in row ] for row in mid ]
        mid=list(zip(*mid))
        
        
        res=[int(''.join(list(map(str,row))),2) for row in mid]
        return sum(res)
        






