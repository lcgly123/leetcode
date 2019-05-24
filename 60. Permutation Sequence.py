60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        '''
        k=17相当于下标16（以后都是以下标0开始算），由于第0位数有6种情况，所以16/6=2，所以第0位数是1,2,3,4的第2位即3，那么剩下16%6=4位，第1位数有2种情况，所以4/2=2，所以第1位数是1,2,4中的4，这时剩下4%2=0，第2位0/1=0，所以第2位是1,2中的1，剩下0%1=0，第3位0/1=0，所以第3位是剩下的2的2，所以最后的数字是3,4,1,2
        '''
        
        import math
        res=[]
        
        choice=[x for x in range(1,n+1)]
        
        while(len(choice)!=0):
            i,k=divmod(k,math.factorial(len(choice)-1))# 阶乘
            if k!=0:
                res.append(str(choice[i]))
                choice.pop(i)
            else:
                res.append(str(choice[i-1]))# 就是为了对应坐标
                choice.pop(i-1)
        
        return ''.join(res)
