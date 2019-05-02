820. Short Encoding of Words

Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        # 题意就是把words变成字符串（加#），不要后缀
        string=''
        
        words.sort(key=lambda x:len(x),reverse=True)
        
        for w in words:
            if w+'#' not in string:# 加‘#’表明是后缀，而不是中间的
                string+=w+'#'
                
        return len(string)
        
