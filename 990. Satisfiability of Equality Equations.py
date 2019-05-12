990. Satisfiability of Equality Equations

Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dic={}# 理解为一个节点（key）指向哪个节点
        # dic=collections.defaultdict(str)# 没必要，还可能出错，因为下面
        
        def get_head(x):# 三种可能，不在dic里，在dic里但不是自环节点，在dic里且是自环节点
            if x not in dic:
                dic[x]=x# 因为这会自己造
            if x!=dic[x]:
                dic[x]=get_head(dic[x])# 会更新一个节点指向的节点
            return  dic[x]
        
        # 不断更新节点的指向
        # 最终，一个集合的节点都会指向一个自环节点（直接或间接）
        # 这和原图的节点有没有环没关系
        for x,e1,e2,y in equations:
            if e1=='=':
                head1=get_head(x)
                head2=get_head(y)
                dic[head1]=head2
        
        for x,e1,e2,y in equations:
            if e1=='!':
                head1=get_head(x)
                head2=get_head(y)
                if head1==head2:
                    return False
        return True
        
