743. Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 这个题要找网络延迟最长的点
        # 其实不难
        import collections
        # 造加权有向图，有用
        gragh=collections.defaultdict(dict)
        for u,v,w in times:
            gragh[u][v]=w
        
        time=[None]*(N+1)# 因为节点从1开始数
        time[K]=0
        queen=[K]
        
        
        while(queen!=[]):
            new_layer=set()# 可能多个节点指向一个
            for node in queen:
                for next_node in gragh[node]:#直接遍历dict其实是遍历dict的key，有用
                    if time[next_node]==None or time[next_node]>time[node]+gragh[node][next_node]:# 表示没来过或者，有更短的路径时才修改
                        time[next_node]=time[node]+gragh[node][next_node]
                        new_layer.add(next_node)# 放在if外面其实可以，但会超时
            queen=list(new_layer)
        
        res=-1
        for i in range(1,N+1):# 遍历各个节点
            if time[i]==None:# 此点无法到达
                return -1
            res=max(res,time[i])
        return res
            
            
        
