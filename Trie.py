from TrieNode import TrieNode


class Trie:

    def __init__(self, root=None):
        self.root = TrieNode(character=None)

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def _splitWord(self, word):
        return list(word)

    def addWord(self, word):
        if self.checkIfWordExists(word):
            raise Exception("The word is already in the dictionary.")
        else:
            wordChars = self._splitWord(word)
            currentChar = wordChars[0]
            currentPos = 0
            currentNode = self.root
            while True:
                if currentChar not in currentNode.children:
                    newNode = TrieNode(character=currentChar, parent=currentNode)
                    currentNode.children[currentChar] = newNode
                    currentPos += 1
                    currentNode = newNode
                    if currentPos < len(wordChars):
                        currentChar = wordChars[currentPos]
                    else:
                        break
                else:  # currentChar in currentNode.children:
                    currentNode = currentNode.children[currentChar]
                    currentPos += 1
                    if currentPos < len(wordChars):
                        currentChar = wordChars[currentPos]
                    else:
                        break
            endWord = TrieNode(character=None, parent=currentNode)
            endWord.isWord = True
            currentNode.children[""] = endWord

    def checkIfWordExists(self, word):
        wordChars = self._splitWord(word)
        wordChars.append("")
        currentChar = wordChars[0]
        currentPos = 0
        currentNode = self.root
        while currentChar in currentNode.children:
            currentPos += 1
            currentNode = currentNode.children.get(currentChar)
            if currentPos < len(wordChars):
                currentChar = wordChars[currentPos]
            else:
                if currentNode.isWord == True:
                    print("The word: " + str(word) + " has been successfully found.")
                    return True

    def _getTheLeaves(self, node):
        children = self._getChildrenList(node)
        leaves = {}
        for char in children:
            charnode = node.children.get(char)
            if charnode.children == {} and charnode.isWord:
                leaf = charnode.parent
                leaves[leaf.character] = leaf
            else:
                leavestemp = self._getTheLeaves(charnode)
                leaves.update(leavestemp)
        return leaves

    def autoCompletion(self, word):
        rootNode = self._getLastNodeOfPrefix(word)
        leaves = self._getTheLeaves(rootNode)
        wordsList = []
        for leaf in leaves.keys():
            currentNode = leaves[leaf]
            wordLetters = []
            while currentNode is not rootNode:
                wordLetters.insert(0, currentNode.character)
                currentNode = currentNode.parent
            tempword = ""
            for letter in wordLetters:
                tempword = tempword + letter
            tempword = word + tempword
            wordsList.append(tempword)
        print("Maybe you mean one of the following:")
        print(*wordsList, sep=', ')
        return wordsList

    def _getChildrenList(self, node):
        if node.children != {}:
            return [*node.children]

    def _getLastNodeOfPrefix(self, word):
        wordChars = self._splitWord(word)
        currentChar = wordChars[0]
        currentPos = 0
        currentNode = self.root
        while currentChar in currentNode.children:
            currentPos += 1
            currentNode = currentNode.children.get(currentChar)
            if currentPos < len(wordChars):
                currentChar = wordChars[currentPos]
        return currentNode

    def lookForOtherWordsInIt(self, word):
        wordChars = self._splitWord(word)
        temp = wordChars[0]
        pos = 0
        wordList = []
        while pos < len(wordChars)-1:
            if self.checkIfWordExists(temp) is True:
                wordList.append(temp)
            pos += 1
            temp = temp + wordChars[pos]
        return wordList

    def deleteWord(self, word):
        if self.checkIfWordExists(word):
            wordChars = self._splitWord(word)
            currentChar = wordChars[0]
            currentPos = 0
            currentNode = self.root
            if self.lookForOtherWordsInIt(word):
                otherWords = self.lookForOtherWordsInIt(word)
                maxWord = max(otherWords, key=len)
                currentNode = self._getLastNodeOfPrefix(maxWord)
                currentChar = wordChars[len(maxWord)]
            while currentChar in currentNode.children:
                tempNode = currentNode.children.get(currentChar)
                currentNode.children.pop(currentChar)
                currentPos += 1
                currentNode = tempNode
                if currentPos < len(wordChars):
                    currentChar = wordChars[currentPos]
                print("The word: " + str(word) + " has been successfully removed.")
                return True



