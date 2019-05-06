870. Advantage Shuffle

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]



class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        
        # 我们先在A中找刚好大于该数的数字（这就是为啥中马跟其下马比，
        # 而不是上马跟其下马比），用太大的数字就浪费了，
        # 而如果A中没有比之大的数字，随便就行
       
        
        a=sorted(A)
        b=sorted(B)
        
        import collections
        match=collections.defaultdict(list)
        no_match=[]
        
        j=0
        for i,_ in enumerate(a):
            if a[i]>b[j]:
                match[b[j]].append(a[i])
                j+=1
            else:
                no_match.append(a[i])
        
        res=[]
        # 注意是B
        for n in B:
            if n in match and len(match[n])>0:
                res.append(match[n].pop())
            else:
                res.append(no_match.pop())# 随便
        
        return res
                
        
        
        
