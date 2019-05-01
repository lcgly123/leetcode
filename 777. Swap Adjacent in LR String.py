777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        # 其实很简单，根据题意，L只能想左移动，R只能向右移动，且不能跨越别的LR
        # 所以AB中LR数目，顺序要相等
        A=[(i,c) for i,c in enumerate(start) if c=='L' or  c=='R']
        B=[(i,c) for i,c in enumerate(end) if c=='L' or  c=='R']
        if len(A)!=len(B):
            return False
        
        for (i,s),(j,e) in zip(A,B):
            if s!=e:
                return False
            if s=='L':
                if i<j:
                    return False
            if s=='R':
                if i>j:
                    return False
        
        return True
        
        
        
