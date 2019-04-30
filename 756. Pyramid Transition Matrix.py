756. Pyramid Transition Matrix

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.



class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        import collections
        dic=collections.defaultdict(list)
        
        for w in allowed:
            dic[w[:2]].append(w[-1])
        
        # 主要麻烦再同一个bootom可以对应多个up，如"XXX", "XXY"
        def dfs(candi):
            if len(candi)==1:
                return True
 
            
            #  其实就得到上一次的排列组合比较麻烦，其他就是一个正常的dfs
        # 求排列组合的方法，自己写的，有用
            next_candi=['']
            for i in range(len(candi)-1):
                if dic[candi[i:i+2]]=='':
                    return False
                mid=[]
                for c in  dic[candi[i:i+2]]:
                    for can in next_candi:
                        mid.append(can+c)
                next_candi=mid[:]
                
                
            for up_layer in next_candi:
                if dfs(up_layer):
                    return True
            return False
        
        return dfs(bottom)
                    
        
