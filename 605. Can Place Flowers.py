605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        a=[0]+flowerbed+[0]#NB
        
        for i in range(1,len(a)-1):
            if a[i-1]==a[i]==a[i+1]==0:
                a[i]=1
                n-=1
            if n==0:
                return True
        
        return False
605. Can Place Flowers

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False




class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        a=[0]+flowerbed+[0]#NB
        
        if n==0:
            return True
        for i in range(1,len(a)-1):
            if a[i-1]==a[i]==a[i+1]==0:
                a[i]=1
                n-=1
            if n==0:
                return True
        
        return False
