686. Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”),
B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        temp=''
        res=0
        while(len(temp)<len(B)):
            temp+=A
            res+=1
        
        # 重复到刚好比B大，再加一个A就能判断了，再加没用了
        if B in temp:
            return res
        if B in temp+A:
            return res+1
        return -1
        
