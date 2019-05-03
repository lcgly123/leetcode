825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.



class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
        # 其实挺简单
        import collections
        dic=collections.Counter(ages)
        
        res=0
        
        for a in dic:
            for b in dic:
                if a==b:
                    if b<=0.5*a+7 :
                        continue
                    else:
                        res+=dic[a]*(dic[b]-1)# 注意
                else:
                    if b<=0.5*a+7 or b>a or (a<100 and b>100):
                        continue
                    else:
                        res+=dic[a]*dic[b]
        
        return res
                
                
        
