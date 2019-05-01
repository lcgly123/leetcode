791. Custom Sort String

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        
        res=[]
        
        # 就是把在S中的全放前面了，NB
        for c in S:
            res.append(c*T.count(c))
        for c in T:
            if c not in S:
                res.append(c)
        
        return ''.join(res)
        
