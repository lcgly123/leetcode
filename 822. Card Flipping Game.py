822. Card Flipping Game

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
#         如果某一张牌的正面和背面的数字是一样的，那么无论翻转还是不翻转，
#         该数字都会出现在正面的，所以该数字不可能为good number。对于其余的数字，
#         我们实际上只需要找出最小值即可，这是由于：一旦该最小值出现在某个牌的正面，
#         我们只需要将该牌翻转即可（由于该牌的正反面不一样，所以将该牌翻转之后
#         ，出现在正面的一定是另外一个数字）。
# --------------------- 
#         我们可以先把正反数字相同的卡片都找出来，将数字放入一个HashSet，
#         也方便我们后面的快速查找。现在其实我们只需要在其他的数字中找到一个最小值即可，
#         因为正反数字不同，就算fronts中其他卡片的正面还有这个最小值，
#         我们可以将那张卡片翻面，使得相同的数字到backs数组，总能使得fronts数组不包含有这个最小值
        
        
        total=set(fronts)|set(backs)#两集合并集
        
        same=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                same.add(fronts[i])
        res=total-same#差集 
        return min(res) if res else 0
        
        
