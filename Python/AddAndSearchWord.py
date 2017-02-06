class Node(object):

    def __init__(self):
        self.isWord = False
        self.branches = {}
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        temp = self.root
        for l in word:
            if l not in temp.branches:
                temp.branches[l] = Node()
            temp = temp.branches[l]
        temp.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, self.root)

    def searchHelper(self, word, root):
        temp = root
        for l in range(len(word)):
            state = False

            # case for .
            if word[l] == '.':
                for i in temp.branches:
                    state = state or self.searchHelper(
                        word[l + 1:], temp.branches[i])
                return state

            if word[l] in temp.branches:
                temp = temp.branches[word[l]]
            else:
                return False
        return temp.isWord

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("abc")
print obj.search("...")
