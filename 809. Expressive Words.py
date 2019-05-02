809. Expressive Words


Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        
        
        def check(s,w):
            j=0
            for i,c in enumerate(s):
                if j<len(w) and s[i]==w[j]:
                    j+=1
                else:

                    if s[i-1:i+2]!=s[i]*3!=s[i-2:i+1]:# 少于2个相等的必符合这个条件，NB
                        return False
            return j==len(w)
        
        return sum(check(S, W) for W in words)
                    
        
