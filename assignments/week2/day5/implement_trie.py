class TrieNode:
    def __init__(self):
        self.children={} #at most 26
        self.end_word=False

class Trie:
    #Time O(1), Space O(1)
    def __init__(self): #constructor
        self.root = TrieNode()

    #Time O(n) where n is size of word, Space O(1)
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        
        curr.end_word = True

    #Time O(n) where n is size of word, Space O(1)
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        
        return curr.end_word # must be the last letter to know word is in tree

    #Time O(n) where n is size of word, Space O(1)
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        
        return True # we don't care if it is the last letter


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)