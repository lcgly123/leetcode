969. Pancake Sorting

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

 

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        """
        找到最大的数字，假设它的下标是i
        反转0到i之间的数字，使得A[i]变成第一个数
        反转整个数组，让最大的数到末尾
        """
        # 和题目不一样，但也对，更好理解
        res=[]
        for i in range(len(A)-1,0,-1):# 到第二个就行了
            cur_max_index=A.index(max(A[:i+1]))
            # print(cur_max_index)
            res.append(cur_max_index+1)# 反转个数
            A[:cur_max_index+1]=list(reversed(A[:cur_max_index+1]))
            res.append(i+1)
            A[:i+1]=list(reversed(A[:i+1]))
            
        return res
