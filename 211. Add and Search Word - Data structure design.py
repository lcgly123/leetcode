211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true


class TrieNode:
    def __init__(self):
        self.is_end=False
        self.chars={}
        

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node=self.root
        for c in word:
            if c not in node.chars:
                node.chars[c]=TrieNode()
            node=node.chars[c]
        node.is_end=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(word,node):
            if word=='':# 注意这一点，字符串最后是‘’不是【】，经常错
                if node.is_end:# 这里不是搜前缀，一定要完整的词
                    return True
                else:
                    return False
            for c in node.chars:
                if c ==word[0] or word[0]=='.':
                    if dfs(word[1:],node.chars[c]):
                        return True
            return False
        
        return dfs(word,self.root)
   
        
