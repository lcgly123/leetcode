56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals==[]:
            return []
        inter=sorted(intervals,key=lambda x:x[0])# 这个很重要
        res=[]
        i=0
        while( i <len(inter)):
            j=i+1
            s,e=inter[i][0],inter[i][1]# 融合模板区间
            while( j<len(inter) and e>=inter[j][0]):
                s=min(s,inter[j][0])
                e=max(e,inter[j][1])
                j+=1
            res.append([s,e])
            i=j
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res=[]
#         if len(intervals)==0:
#             return []
        
#         intervals=sorted(intervals,key=lambda i:i.start)# 要先做个排序
#         temp=intervals[0]
#         for i in range(len(intervals)-1):
#             if intervals[i+1].start<=temp.end and intervals[i+1].end>=temp.start:
#                 if intervals[i+1].start<=temp.start:
#                     temp.start=intervals[i+1].start
#                 if intervals[i+1].end<=temp.end:
#                     temp.end=temp.end
#                 else:
#                     temp.end=intervals[i+1].end
#             else:
#                 res.append(temp)
#                 temp=intervals[i+1]
                
#         if intervals[-1].start<=temp.end and intervals[-1].end>=temp.start:
#             if intervals[-1].start<=temp.start:
#                 temp.start=intervals[-1].start
#             if intervals[-1].end<=temp.end:
#                 temp.end=temp.end
#             else:
#                 temp.end=intervals[-1].end
#         res.append(temp)
                
#         return res
                
