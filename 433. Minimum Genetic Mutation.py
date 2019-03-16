433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
 

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def check(s1,s2):
            if len(s1)!=len(s2):
                return False
            cou=0
            for i in range(len(s2)):
                if s1[i]!=s2[i]:
                    cou+=1
            if cou==1:
                return True
            else:
                return False
        
        def dfs(candidate,start,end,path,res):
            if path!=[]:
                if path[-1]==end:
                    res.append(path)
                    return 
            if candidate==None:
                return 
            
            for i in range(len(candidate)):
                if check(candidate[i],start):
                    can_in =candidate[:]
                    can_in.pop(i)
                    dfs(can_in ,candidate[i],end,path+[candidate[i]],res)
             
        res=[]
        dfs(bank,start,end,[],res)
        
        if res==[]:
            return -1
        else:
            return min([len(x) for x in res])
        
