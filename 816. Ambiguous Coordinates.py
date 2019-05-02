816. Ambiguous Coordinates

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation: 
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: "(100)"
Output: [(10, 0)]
Explanation: 
1.0 is not allowed.


class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
# 有用
# '''
#     •itertools.combinations('abcd',2)

#         这个方法从序列abcd中任选两个进行组合，返回一个迭代器，以tuple的形式输出所有组合，如('a','b'),                ('a','c')等等。总共是C24 =6种组合

#     •itertools.permutations（'abc',2）

#         和combinations类似，为排序，输出的迭代器，里面内容是('a','b'),('b','a')等等，一共是A2 3=6种组合

#     •itertools.product('abc','123')

#         相当于是下面这样的代码

#     for element1 in list1:
#         for element2 in list2:
#             yield element1,element2
# '''
        
        def valid(s):
            # str(int(s))==s会去除开头为0 的数
            if s=='0':
                return True
            if s[0]=='0' and s[-1]=='0':
                return False
            return True
        def partion(s):
            res=[]
            for i in range(1,len(s)):
                if valid(s[:i]) and valid(s[i:]):
                     res.append([s[:i],s[i:]])
            return res
        
        def adddot(s):
            res=[]
            
            if len(s)==1:
                res.append(s)
            elif s[0]=='0':
                res.append(s[0]+'.'+s[1:])
            elif s[-1]=='0':
                res.append(s)
            else:
                for i in range(1,len(s)):
                    res.append(s[:i]+'.'+s[i:])
                res.append(s)
            return res
        s=S[1:-1]
        nums=partion(s)
        res=[]
        import itertools
        for num1,num2 in nums:
            print( num1,num2)
            print(adddot(num1))
            res+=[ '('+x+', '+y+')' for x,y in itertools.product(adddot(num1),adddot(num2))]
            
        
        return res
        
                    
                    
            
            
            
                                         
                                         
        
        
