714. Best Time to Buy and Sell Stock with Transaction Fee

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold=[0]*len(prices)# 这个节点决定持有，手里最多有多少钱，下面类似
        unhold=[0]*len(prices)
        hold[0]=-prices[0]
        
        for i in range(1,len(prices)):
            hold[i]=max(hold[i-1],unhold[i-1]-prices[i])
            unhold[i]=max(unhold[i-1],hold[i-1]+prices[i]-fee)
        return unhold[-1]
            
        
