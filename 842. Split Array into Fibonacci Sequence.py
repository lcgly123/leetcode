842. Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        # 答案不如我的好
        def check(index,res):
            if index==len(S):
                return True
            n3=str(res[-1]+res[-2])
            # if res[0]==123 and res[1]==456:
                # print(res,n3)
            if S[index:index+len(n3)]==n3 and int(n3)<2 ** 31 - 1:#  and int(n3)<2 ** 31 - 1这个加上就对了
                res.append(int(n3))
                flag=check(index+len(n3),res)
                return flag
            else:
                return False
            
            
        
        
        for i in range(1,len(S)-1):
            for j in range(i+1,len(S)):
                n1=S[:i]
                n2=S[i:j]
                
                if str(int(n1))!=n1 or str(int(n2))!=n2:
                    continue
                res=[int(n1),int(n2)]
                flag=check(j,res)
                # print(n1,n2,flag)
                if flag: 
                    return res
        return []
                    
        
        
        
        
