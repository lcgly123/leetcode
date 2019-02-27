313. Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.



class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        index=[0 for i in range(len(primes))]
        ugly_num=[1]
        
        for i in range(1,n):
            num=min([ugly_num[index[j]]*primes[j] for j in range(len(index))])
            ugly_num.append(num)
            
            for i in range(len(primes)):# 把所有可能的选项都更新，防止出现重复的值，正常就应该这样
                if(ugly_num[-1]==ugly_num[index[i]]*primes[i]):
                    index[i]+=1
            
        return ugly_num[-1]
