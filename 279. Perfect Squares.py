279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


class Solution:
    def numSquares(self, n: int) -> int:
        # 可以但会超时
        import math
        
        def bfs(n):
            
            queen=[i*i for i in range(1,int(math.sqrt(n)+1)) if i*i<=n and i!=0]
            path=[[i] for i in queen]
            

            while(queen):
                new_layer=[]
                new_path=[]
                for i in range(len(queen)):

                    temp=n-sum(path[i])
                    if temp==0:
                        return len(path[i])
                    for j in range(1,int(math.sqrt(temp))+1):
                        if j*j<=temp :
                            new_layer.append(j*j)
                            new_path.append(path[i]+[j*j])

                queen=new_layer
                path=new_path
                
        res=bfs(n)
        
        return res
                

