436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals: List[Interval]) -> List[int]:
        with_index=[[x.start,x.end,i] for i,x in enumerate(intervals)]
        p1=sorted(with_index,key=lambda x:x[0])
        
        
        res=[-1]*len(p1)
        for i in range(len(p1)):
            if i==len(p1)-1:
                res[p1[i][-1]]=-1
            else:
                l,r=i+1,len(p1)-1# 有用，二分法查找
                while(l<r):
                    mid=(l+r)//2
                    if p1[i][1]<=p1[mid][0]:
                        r=mid
                    elif p1[i][1]>p1[mid][0]:
                        l=mid+1
                        
                        
                res[p1[i][-1]]=p1[l][-1] if p1[i][1]<=p1[l][0] else -1

        return res
        #会超时
#         with_index=[[x.start,x.end,i] for i,x in enumerate(intervals)]
#         p1=sorted(with_index,key=lambda x:x[0])
        
        
#         res=[-1]*len(p1)
#         for i in range(len(p1)):
#             if i==len(p1)-1:
#                 res[p1[i][-1]]=-1
#             else:
#                 j=1+i
#                 while(j<len(p1)):
#                     if p1[i][1]>p1[j][0]:
#                         j+=1
#                     else:
#                         res[p1[i][-1]]=p1[j][-1]
#                         break

#         return res
            
