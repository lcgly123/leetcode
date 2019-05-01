779. K-th Symbol in Grammar

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001



 			            0
 	           0                 1
             0    1            1     0
           0 1    1 0         1  0    0  1
           
           
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        # 规律，左节点不变化，右节点变化
        # 倒着数，看变化的情况，flag==1，说明与原点一样，否则不一样
        # 这里k，n不代表坐标
        flag=1
        for i in range(N-1):
            if K%2==0:
                flag=-flag
                K/=2
            else:
                K=(K+1)/2
        
        return 0 if flag==1 else 1
        
