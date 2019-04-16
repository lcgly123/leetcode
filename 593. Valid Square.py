593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True



class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 四条边相等，对角线相等且为边的2倍
        def dist(p1,p2):
            return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        
        dis=[dist(p1,p2),dist(p2,p3),dist(p3,p4),dist(p1,p3),dist(p2,p4),dist(p4,p1)]
        dis.sort()
        
        return 0<dis[0]==dis[1]==dis[2]==dis[3] and 2*dis[0]==dis[4]==dis[5]
