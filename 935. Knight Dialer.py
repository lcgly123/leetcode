935. Knight Dialer

A chess knight can move as indicated in the chess diagram below:

This time, we place our chess knight on any numbered key of 
a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

class Solution:
    def knightDialer(self, N: int) -> int:
        # NB
        #马的初始位置可以在拨号按键的任意位置，现在要让它走N - 1步，问这个马能产生出多少种不同的拨号号码？
        # 每一个初始位置都要算
        # 每个键下一步走哪，灰色的不能走
        dic={1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        
        dp=[1]*10
        
        for _ in range(N-1):
            new=[0]*10 # NB
            for i in range(10):# 代表前面一步的结果
                for j in dic[i]:
                    new[j]+=dp[i]
            dp=new
        
        return sum(dp) % (10 ** 9 + 7)
                    
        
