问题：前缀树建立，查找

例题：208

class TrieNode:
    def __init__(self):
        self.is_end=False # 
        self.children={}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()# 会把前面的覆盖掉
            node=node.children[c]
        node.is_end=True
        return
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for c in word:
            if c not in node.children:
                return False
            node=node.children[c]
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for c in prefix:
            if c not in node.children:
                return False
            node=node.children[c]
        return True
        
