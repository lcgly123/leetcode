911. Online Election
Medium

164

107

Favorite

Share
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.p=persons
        self.t=times
        
        import collections
        dic=collections.defaultdict(int)
        
        self.winner=[]
        lead=0
        for t,p in list(zip(self.t,self.p)):#NB
            dic[p]+=1
            if dic[p]>=dic[lead]:# 等于就换人，题意，没办法
                lead=p
            self.winner.append(lead)
            

    def q(self, t: int) -> int:
        import bisect
        
        return self.winner[bisect.bisect(self.t, t) -1]# 相等就插右边
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
