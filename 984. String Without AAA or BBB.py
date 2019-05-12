984. String Without AAA or BBB

Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        
        # 前提是：不会出现不可能的情况
        def make(A,B):
            if A>=2*B:
                return 'aab'*B+'a'*(A-2*B)# 前提是：不会出现不可能的情况
            elif A>=B:
                return 'aab'*(A-B)+'ab'*(B-(A-B))
            elif B>=2*A:
                return 'bba'*A+'b'*(B-2*A)
            else:
                return 'bba'*(B-A)+'ba'*(A-(B-A))# 这‘ab’‘ba’都可以
        
        return make(A,B)
        

