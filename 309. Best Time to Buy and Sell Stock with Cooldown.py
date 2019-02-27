309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nothold,cooldown,hold=0,float('-inf'),float('-inf')#注意无穷的写法
        # 三种状态，持有股票，不持有股票，冷静期，用状态机画出来确实更好理解
        for p in prices:#是这一步和上一步之间进行操作股票的价格
            nothold,cooldown,hold=max(cooldown,nothold),hold+p,max([nothold-p,hold])# 持有之后不会再买了
            
        return max(nothold,cooldown)

