739. Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].



class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(T)
        
        # 其实就是找下一个比该点大的数，求他俩的距离
        # 栈NB，之前见过这种用法
        for i,t in enumerate(T):
            while(stack and T[stack[-1]]<t):
                last_i=stack.pop()
                res[last_i]=i-last_i
            stack.append(i)
        return res
