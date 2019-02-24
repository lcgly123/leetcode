290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false



class Solution:
    def wordPattern(self, pattern: str, str_: str) -> bool:
        
        s=str_.split()
        if len(pattern)!=len(s):
            return False
        # NB
        return len(set(s))==len(set(pattern))==len(set(list(zip(s,pattern))))









