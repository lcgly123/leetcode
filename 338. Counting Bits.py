338. Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]

class Solution:
    def countBits(self, num: int) -> List[int]:
        # 其实很简单，如果一个数是另一个数的2倍，就是左移一位，1的个数是一样的，奇数就加1
        res=[0]
        for i in range(1,num+1):
            temp=res[i//2]+i%2
            res.append(temp)
            
        return res

