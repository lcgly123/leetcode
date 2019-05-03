838. Push Dominoes

There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.



class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 如果当前字符是’.’，那么跳过，如果当前字符是’L’，判断上一次字符last是什么，
        # 如果last是’L’，那么就把last到当前字符位置的字符全部赋值为’L’，如果last是’R’，
        # 那么前面一半位置赋值为’R’,后面一半位置赋值为’L’，中间赋值为’.’，最后更新last为当前的字符。
        # 当前字符是’R’时，如果last是’R’,那么把last到当前字符位置全部赋值为’R’, 如果last是’L’，
        # 那么则不做处理（因为last向左倒，当前向右倒），最后更新last的字符和位置。
        # 时间复杂度分析：需要扫描一遍数组，复杂度为O(n)
        # 其实不难
        
        last_i=0
        last_c='.'
        res=list(dominoes)
        
        for i,c in enumerate(dominoes):
            if c=='.' and i!=len(dominoes)-1:# 防止最后一个。
                continue
            elif c=='L':
                if last_c=='L':
                    j=last_i+1
                    while(j<i):
                        res[j]='L'
                        j+=1
                elif last_c=='R':
                    l,r=last_i+1,i-1
                    while(l<r):
                        res[l],res[r]='R','L'
                        l+=1
                        r-=1
                    if l==r:
                        res[l]='.'
                elif last_c=='.':
                    j=0
                    while(j<i):
                        res[j]='L'
                        j+=1
                last_c='L'
                last_i=i
            elif c=='R':  # 必须有条件，因为第一个条件
                if last_c=='R':
                    j=last_i+1
                    while(j<i):
                        res[j]='R'
                        j+=1
                last_c='R'
                last_i=i
                
            if i==len(dominoes)-1 and dominoes[i]=='.' and last_c=='R':
                j=last_i+1
                while(j<len(dominoes)):
                    res[j]='R'
                    j+=1
                
        return ''.join(res)
        
        
