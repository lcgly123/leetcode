556. Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
#         这里分三步：
#         1、从右向左找第一个不符合升序的数，记录其前一个位置为index，如果没有，返回-1

#         2、从右到index+1找第一个比他大的数，交换index位置的数和这个比他大的数

#         3、从index+1到末尾进行升序排列
        
        nums=map(int,list(str(n)))
        index=len(nums)-1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                index=i-1
                break
        if index==len(nums)-1:
            return -1
        
        print(index)
        for j in range(len(nums)-1,index,-1):
            if nums[j]>nums[index]:
                print(j)
                nums[j],nums[index]=nums[index],nums[j]
                nums[index+1:]=sorted(nums[index+1:])
                break
        res=int(''.join(map(str,nums)))
        return  res if res.bit_length() <= 31 else -1 # 只是题目要求不溢出
        
        
