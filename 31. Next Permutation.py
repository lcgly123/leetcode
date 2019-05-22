31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 算法是这样：倒着找到第一个值比它后面值小的（这里是nums[r-1]），
        # 和依然是倒着数第一个值比它大的交换（这里是nums[insert_i）
        # 再从r开始排序（从小到大）
        # 就是比第一个比原排列大的排列，或者循环过来
        r=len(nums)-1
        while(r>0):
            if nums[r]<=nums[r-1]:
                r-=1
            else:
                break
       
        insert_i=len(nums)-1
        while(insert_i>=r):
            if nums[r-1]<nums[insert_i]:
                nums[r-1],nums[insert_i]=nums[insert_i],nums[r-1]
                break
            insert_i-=1
            
        nums[r:]=sorted(nums[r:])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def reverse(x,l,r):
#             while(l<r):
#                 x[l],x[r]=x[r],x[l]
#                 l+=1
#                 r-=1
                
                
                
#         r=len(nums)-1
#         while(r>0):
#             if nums[r]<=nums[r-1]:
#                 r=r-1
#             else:
#                 break
        
#         if r==0:# 这个是必须的，因为下面会用到r-1
#             reverse(nums,r,len(nums)-1)
#             return

#         mid_r=len(nums)-1
#         while(mid_r>=r):
#             if  nums[r-1]<nums[mid_r]:
#                 nums[r-1],nums[mid_r]= nums[mid_r],nums[r-1]
#                 break
#             mid_r-=1
        
#         reverse(nums,r,len(nums)-1)
        
#         return 
    
            
