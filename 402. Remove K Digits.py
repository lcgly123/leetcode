402. Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num)==1:
            return '0'
        num=list(map(int,num))
        
        while(k>0):
            k-=1
            
            for i in range(len(num)-1):# 所以这是应对for循环完全不循环的技巧
                if num[i]>num[i+1]:
                    num.pop(i)
                    break
            else:# 循环完会执行这个，break就不会,如果没有，就pop最后一个(必须这样，不然如果全删的话，最后一个删不掉)
                num.pop()
        if len(num)==0:
            return '0'
        return str(int(''.join(list(map(str,num)))))
        

#         if len(num)==1:
#             return '0'
#         while(k!=0):
#             k-=1
            
#             for i in range(len(num)-1):
#                 if num[i]>num[i+1]:# 只要把这种删了就行，好像见过，不懂为啥
#                     num_=list(num)
#                     num_.pop(i)
#                     num=''.join(num_)
#                     break
#             else:# 循环完会执行这个，break就不会,如果没有，就pop最后一个
#                 num_=list(num)
#                 num_.pop()
#                 num=''.join(num_)
#         if len(num)==0:
#             return '0'
#         return str(int(num))
            
