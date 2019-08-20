611. Valid Triangle Number

Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3



class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)# 必须从大到小
        count=0
        # 两指针，好使，3个经常这个
        for i in range(len(nums)-2):#第一条边
            l,r=i+1,len(nums)-1
            while(l<r):
                if nums[i]-nums[l]<nums[r]:
                    count+=r-l
                    l+=1
                else:
                    r-=1
        return count
        












