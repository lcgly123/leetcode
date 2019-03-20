477. Total Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.



class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 累计汉明距离和0跟1的个数，我们可以发现其实就是0的个数乘以1的个数
        strs=['{:032b}'.format(i) for i in nums]
        bits_list=zip(*strs)# 这样就可以，zip的输入为两个或多个tuple
        
        res=0
        for i in list(bits_list):
            res+=i.count('0')*i.count('1')
            
        return res
        
        
