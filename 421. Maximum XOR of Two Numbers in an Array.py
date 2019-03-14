421. Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor=0
        get_former_bit=0
        for i in range(31,-1,-1):
            prob_max=max_xor|1<<i# 假设可能的最大值第i位是1
            
            # 得到前面的几个bits
            get_former_bit=get_former_bit|1<<i
            bits_all=set()
            for num in nums:
                bits_all.add(num&get_former_bit)
            for bits in bits_all:# 最大值^ bits_all中的元素一定还在bits_all中，因为max=a^b(a,b in bits_all),由异或性质知，必有a^max=b in bits_all,NB
                if bits^prob_max in bits_all:
                    max_xor=prob_max
                    break
        
        return max_xor
          
                
                
        
