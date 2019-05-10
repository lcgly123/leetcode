966. Vowel Spellchecker

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:



class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        # 题意：给定一个词，看看是否在字典里，再看看其小写是否字典里某个小写相同（有多个取第一个），再
        # 看看是否与字典里某个只是元音不同（不分大小写），返回该词在字典里的对应词，不然返回‘’
        
        # 查询的题一般都用字典，多加几个字典
        # 代码写的比较乱
        lowers={}
        convert={}
        wordset=set(wordlist)
        for w in wordlist:
            new_w=w.lower()
            if new_w not in lowers:# 防止被后面同样的改变
                lowers[new_w]=w
            new_c=''.join([c if c not in 'aeiou' else '*' for c in new_w ])
            if new_c not in convert:
                convert[new_c]=w# if在前面
        
        res=[]
        for w in queries:
            if w in wordset:
                res.append(w)
            elif w.lower() in lowers:
                res.append(lowers[w.lower()])
            elif ''.join([c if c not in 'aeiou' else '*' for c in w.lower() ]) in convert:
                res.append(convert[''.join([c if c not in 'aeiou' else '*' for c in w.lower() ])])
            else:
                res.append('')
                
        return res
                
        
