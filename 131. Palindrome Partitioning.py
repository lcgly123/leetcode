131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(s):
            l,r=0,len(s)-1
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def dfs(can,path,res):
            if len(can)==0:
                res.append(path)
                return
            for i in range(1,len(can)+1):
                if is_pal(can[:i]):
                    dfs(can[i:],path+[can[:i]],res)
                    
        res=[]
        dfs(s,[],res)
        return res
