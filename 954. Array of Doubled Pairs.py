954. Array of Doubled Pairs

Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

 

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false




class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        
        import collections
        dic=collections.Counter(A)
        keys=sorted(A,key=abs)#NB,注意是A
        print(dic)
        for n in keys:
            if dic[n] and dic[2*n]:
                dic[n]-=1
                dic[2*n]-=1
        print(dic)
        return all([dic[x]==0 for x in keys])
        
        # 会超时
        # A.sort(key=lambda x:abs(x))
        # while(A):
        #     # print(A)
        #     if A[0]*2 in A:
        #         A.pop(A.index(A[0]*2))
        #         A.pop(0)
        #     else:
        #         return False
        # return True
        
        
        
        
