524. Longest Word in Dictionary through Deleting

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"




class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        # 没有错，题有问题
        long=-1
        index=-1
        for i,w in enumerate(d):
            j=0
            for c in s:
                if c==w[j]:
                    j+=1
                if j==len(w):
                    if len(w)>long:
                        long=len(w)
                        index=i
                    elif len(w)==long:
                        if w<d[index]:
                            long=len(w)
                            index=i
                    break
                # if j == len(word) :
                #     longest = min(longest, word, key=lambda x: (-len(x), x))# NB
                #     break
                
                

        if d==[]:
            return ''
        if index==-1:
            return ''
        return d[index]
            
        
        
        
        













