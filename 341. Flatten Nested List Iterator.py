341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list=[]
        def dfs(candidates,res):
            if isinstance(candidates,int):
                res.append(candidates)
                return
            if isinstance(candidates,list):
                for i in candidates:
                    dfs(i,res)
            else:
                if candidates.isInteger():
                    dfs(candidates.getInteger(),res)
                for i in candidates.getList():
                    dfs(i,res)

            
        dfs(nestedList,self.list)
        
        self.p=0
        

    def next(self):
        """
        :rtype: int
        """
        if self.p==len(self.list):
            return None
        else:
            self.p+=1
            return self.list[self.p-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p!=len(self.list)
        
