6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # 特例
        if numRows == 1 :
            return s
        
        
        res=['']*numRows
        row=0
        move=1
        
        for x in s:
            res[row]+=x
            if row==0:
                move=1
            elif row==numRows-1:
                move=-1
            row+=move
        
        return ''.join(res)

        
        
#         # s[index]的index=(numRows-1)*n+r
#         # 分两种情况：n为偶数时，是正着数，n为奇数，是倒着数
#         # r是第几行
        
#         out=['']*numRows
        
#         if numRows==1:
#             out[0]+=s
#         else:
#             for index,char in enumerate(s):
#                 if (index//(numRows-1))%2==0:
#                     out[index%(numRows-1)]+=s[index]
#                 else:
#                     out[numRows-1-index%(numRows-1)]+=s[index]
                
#         return ''.join(out)
        
        
