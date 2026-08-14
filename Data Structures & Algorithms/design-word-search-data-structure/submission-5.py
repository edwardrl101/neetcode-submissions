class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                node = self.TrieNode()
                cur.children[c] = node
            cur = cur.children[c]
        cur.is_end = True

    


    def search(self, word: str) -> bool:
        cur = self.root
        def searchRecursive(i: int, cur: TrieNode) -> bool:
            if i == len(word):
                return cur.is_end
            if word[i] == '.':
                ans = False
                for c in cur.children.values():
                    ans = ans or searchRecursive(i+1, c)
                    if ans:
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False
                return searchRecursive(i+1, cur.children[word[i]])
        return searchRecursive(0, cur)
                
        
