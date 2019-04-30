767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""



class Solution:
    def reorganizeString(self, S: str) -> str:
        
        import collections
        c=collections.Counter(S)#有用
        max_c,max_count=c.most_common()[0]
        
        res=[max_c]*max_count
        # 其实就是找出出现最多的，然后把别的插进去
        i=0
        for other_c in c.keys():
            if other_c != max_c:
                for _ in range(c[other_c]):
                    res[i%len(res)]+=other_c# 注意，res是list不是str，元素是str，，NB
                    i+=1
        return ''.join(res) if i >= max_count-1 else ""
        
        
        










