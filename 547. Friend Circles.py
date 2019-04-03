547. Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        def dfs(root,seen):
            if root in seen:
                return
            
            seen.append(root)
            for i,node in enumerate(M[root]):
                if  node==1:
                    dfs(i,seen)
        
        seen=[]
        res=0
        for i in range(len(M)):
            if i not in seen:# 其实就是一个一个找，见过的就过
                dfs(i,seen)
                res+=1
                
        return res
