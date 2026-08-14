class PrefixTree:

    class TrieNode():
        def __init__(self, char = "", valid = False):
            self.char = char
            self.valid = valid
            self.children = {}
        
        def addChild(self, child):
            self.children[child.char] = child

    def __init__(self):
        self.root = self.TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] in cur.children:
                cur = cur.children[word[i]]
            else:
                node = self.TrieNode(word[i], False)
                cur.addChild(node)
                cur = node
        cur.valid = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            if word[i] in cur.children:
                cur = cur.children[word[i]]
            else:
                return False
        return cur.valid

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] in cur.children:
                cur = cur.children[prefix[i]]
            else:
                return False
        return True
