853. Car Fleet

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.



 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 题意：好多车，如果后面的赶上前面的就变成一辆，问最后一共几辆
        #NB
        time=[(target-p)/s for p,s in sorted(zip(position,speed),reverse=True)]#pos大，距离target近
        
        
        res=0
        cur_t=0
        for t in time:
            if t>cur_t:
                res+=1
                cur_t=t
        return res
        
        
        
        
