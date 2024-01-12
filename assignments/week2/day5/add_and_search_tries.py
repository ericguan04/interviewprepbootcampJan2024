class TrieNode:
    def __init__(self):
        self.children={} #at most 26
        self.end_word=False

class WordDictionary:

    # Very similar to Implement Trie (Prefix Tree) problem:
    # We first create the Trie class ad use hashmaps.
    # Adding words to the trie is exactly the same, but we need to use recursion and backtracking to account for the '.' case.

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        
        curr.end_word = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    #we need to use backtracking recursion to do this part
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.end_word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)