638. Shopping Offers

In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy for each item. The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        memo={}
        def dfs(price,special,need):
            if need in memo:
                return memo[need]
            
            
            cost=0
            for i,n in enumerate(need):
                cost+=price[i]*n
            
            for choose in special:
                for i,n in enumerate(need):
                    # print(need,choose)
                    if n<choose[i]:
                        break
                else:# 执行完上面的就会执行下面的,表示这个choose可以，本题意思是不能多买，其实没有证明
                    new_need=[need[i]-choose[i] for i in range(len(need))]
                    new_need=tuple(new_need)
                    cost=min(cost,choose[-1]+dfs(price,special,new_need))
            memo[need]=cost
            return cost
        
        memo={}
        res=dfs(price,special,tuple(needs))
        
        return res
                    
            
