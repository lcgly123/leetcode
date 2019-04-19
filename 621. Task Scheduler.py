621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        import collections
        dic=collections.defaultdict(int)
        
        max_freq=0
        max_freq_count=0
        for c in tasks:
            dic[c]+=1
            
            if dic[c]>max_freq:
                max_freq=dic[c]
                max_freq_count=1# 出现频率最大的为1
            elif dic[c]==max_freq:
                max_freq_count+=1# 出现频率最大的更多了
                
        if len(dic)<=n+1:# 有重复项，要这么计算，因为需要间隔
            return (max_freq-1)*(n+1)+max_freq_count# 隔n个，则前面一个组合为n+1个，最后要加上出现最多的几个字母
        else:
            return max(len(tasks),(max_freq-1)*(n+1)+max_freq_count)# len(dic)表示没有重复，没有间隔可以直接这么算
        
        
