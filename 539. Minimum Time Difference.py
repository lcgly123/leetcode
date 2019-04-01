539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # 可以，NB
        minites=[int(x.split(':')[0])*60+int(x.split(':')[1]) for x in timePoints]
        minites.sort()
        minites.append(minites[0]+24*60)
        res=float('inf')
        for i in range(1,len(minites)):
            res=min(res,minites[i]-minites[i-1])
            
        return res
            
        
