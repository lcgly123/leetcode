881. Boats to Save People

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)




class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l=0
        # 超过限制，就只救一个人，l只是能减少运送次数
        
        for r in range(len(people)-1,-1,-1):
            if people[l]+people[r]<=limit:
                l+=1
            if l>=r:
                return len(people)-r
        
        






