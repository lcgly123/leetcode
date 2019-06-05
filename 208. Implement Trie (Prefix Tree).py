208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.
Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true


class node(object):
    def __init__(self,val):
        self.children={}
        self.is_end=False



class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=node()
        

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=node()
            cur=cur.children[c]
        cur.is_end=True
        

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.is_end

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True
