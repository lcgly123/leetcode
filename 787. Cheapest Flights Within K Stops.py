787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        

#         # NB
#         dp=[float('inf')]*n
#         dp[src]=0
        
#         for _ in range(K+1):# k个stop则中间一共k+1个空
#             new_dp=dp[:]# 注意，不然前面改的影响后面的
#             for s,d,cost in flights:
#                 new_dp[d]=min(new_dp[d],dp[s]+cost)
#             dp=new_dp[:]
                
#         return dp[dst] if dp[dst]!=float('inf') else -1
        
        
        gragh=collections.defaultdict(dict)

        for k,v,w in flights:
            gragh[k][v]=w
      

        queen=[(src,1,0)]
        max_step=K+2
        min_cost=float('inf')
        stop=1
        while(queen):
            node,step,cost=queen.pop(0)
            if  node==dst:
                min_cost=min(min_cost,cost)

            for next_node in gragh[node]:
                if min_cost>cost+gragh[node][next_node] and step+1<=max_step:
                    queen.append((next_node,step+1,cost+gragh[node][next_node]))
        return min_cost if min_cost!=float('inf') else -1
            

        

        

        
        
