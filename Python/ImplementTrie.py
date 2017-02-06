class TrieNode(object):

    def __init__(self):
        self.isWord = False
        self.branches = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp = self.root
        for l in word:
            if l not in temp.branches:
                temp.branches[l] = TrieNode()
            temp = temp.branches[l]
        temp.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp = self.root
        for l in word:
            if l in temp.branches:
                temp = temp.branches[l]
            else:
                return False
        return temp.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        print "startsWith:", prefix
        temp = self.root
        for l in prefix:
            if l in temp.branches:
                temp = temp.branches[l]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("hi")
# print obj.startsWith("hi")
print obj.search("h")
