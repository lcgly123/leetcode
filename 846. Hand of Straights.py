846. Hand of Straights

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].



class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        #NB
        hand.sort()
        
        while(hand):
            try:
                base=hand[0]
                for i in range(W):
                    hand.remove(base+i)
            except:
                return False
        
        return True
                
            
        
