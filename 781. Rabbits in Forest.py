781. Rabbits in Forest

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        # 如果某个兔子回答的数字是x，那么说明森林里共有x+1个相同颜色的兔子，
        # 我们最多允许x个兔子同时回答x个，一旦超过了x个兔子，那么就得再增加了x+1个新兔子了。
        # 所以，遇到一个就减一，为0时删掉这个键，再有兔子喊n就是新的颜色
        
        
        
        
        samecolor_num={}
        res=0
        for n in answers:
            if n not in samecolor_num:
                res+=(1+n)
                samecolor_num[n]=n
            else:
                samecolor_num[n]-=1
            if samecolor_num[n]==0:
                del samecolor_num[n]
                
        return res
        
