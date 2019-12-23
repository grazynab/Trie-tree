class TrieNode:

    def __init__(self, character, parent=None):
        self.character = character
        self.parent = parent
        self.children = {}
        self.isWord = False

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, character):
        self.__character = character

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children

    @property
    def isWord(self):
        return self.__isWord

    @isWord.setter
    def isWord(self, isWord):
        self.__isWord = isWord
