901. Online Stock Span

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], 
then the stock spans would be [1, 1, 1, 2, 1, 4, 6].


class StockSpanner:

    def __init__(self):
        self.list=[]
        

    def next(self, price: int) -> int:
        # 给一个股票价格的数组，写一个函数计算每一天的股票跨度，
        # 股票跨度是从当天股票价格开始回看连续的比当天价格低的最大连续天数。
        
        count=1# 小于等于price的天数包括本天
        while len(self.list)>0 and self.list[-1][0]<=price:
            count+=self.list[-1][1]
            self.list.pop()
        self.list.append((price,count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
