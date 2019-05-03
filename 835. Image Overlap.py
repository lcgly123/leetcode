835. Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.



class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        # 由于只有值为1的地方才有可能重叠，所以我们只关心A和B中值为1的地方，
        # 将其坐标位置分别存入两个数组listA和listB中。由于对于A和B中的任意两个1的位置，
        # 肯定有一种方法能将A平移到B，平移的方法就是横向平移其横坐标之差，竖向平移其纵坐标之差。
        # 由于其是一一对应关系，所以只要是横纵坐标差相同的两对儿位置，一定是在同一次平移上。
        
        a,b=[],[]
        import collections
        d=collections.defaultdict(int)
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    a.append((i,j))
                    
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]==1:
                    b.append((i,j))
        
        res=0
        for ax,ay in a:
            for bx,by in b:
                dis=(ax-bx,ay-by)
                d[dis]+=1
                
                res=max(res,d[dis])
                
        return res
        
        





