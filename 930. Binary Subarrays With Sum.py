930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # 和560题一模一样，答案都没变
        nums=A
        k=S
        # 连续子串经常用累加的方法
        dic=collections.defaultdict(int)
        dic[0]=1
        
        res,num_sum=0,0
        for n in nums:
            num_sum+=n
            if num_sum-k in dic:# 如果sum-k在，就有连续子串为k
                res+=dic[num_sum-k]
            dic[num_sum]+=1# 有0的话会多次到达一个地点，有多少次，就有多少可能
            
        return res
