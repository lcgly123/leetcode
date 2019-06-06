306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
             
             
             
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1,len(num)//2+1):
            for j in range(i+1,len(num)):
                # 其实只需要找到前两个数字，后面的滚下去就行
                if (num[:i].startswith('0') and len(num[:i])>1) or (num[i:j].startswith('0') and len(num[i:j])>1):
                    continue
                f=num[:i]
                s=num[i:j]
                r=j
                while(r<=len(num)):
                    temp=str(int(f)+int(s))
                    if not num[r:].startswith(temp):
                        break
                    else:
                        f=s
                        s=temp
                        r=r+len(temp)
                        if r==len(num):
                            return True
        return False
                    
        
