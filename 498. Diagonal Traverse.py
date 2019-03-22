498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        dic=collections.defaultdict(list)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dic[i+j].append(matrix[i][j])# 一斜列,有用
                
        res=[]
        for k in sorted(dic.keys()):
            if k%2==0:
                dic[k].reverse()
                res+=dic[k]
            else:
                res+=dic[k]
                
        return res
