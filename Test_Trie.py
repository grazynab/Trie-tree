import pytest
from Trie import Trie


class TestTrie:

    @pytest.fixture()
    def trie(self):
        trie = Trie()
        return trie

    @pytest.fixture()
    def word(self, trie):
        word = trie.addWord("word")
        return word

    @pytest.fixture()
    def words(self, trie):
        words = trie.addWord("words")
        return words

    @pytest.fixture()
    def wordy(self, trie):
        wordy = trie.addWord("wordy")
        return wordy

    def test_splitWord(self):
        #given
        trie = Trie()
        resultlist = ["w", "o", "r", "d"]

        #when
        testlist = trie._splitWord("word")

        #then
        assert testlist == resultlist

    def test_checkIfWordExists(self, trie, word):  # ShouldReturnTrueWhenWordAdded?
        assert trie.checkIfWordExists("word") is True

    def test_ifCanAddWordWithSamePrefix(self, trie, word, words):
        assert trie.checkIfWordExists("words") is True

    def test_ifCanAddShorterWord(self, trie, words, word): #czy ta kolejność ma znaczenie?
        assert trie.checkIfWordExists("word") is True

    def test_deleteWord(self, trie, word):
        #given
        inputWord = "word"
        # when
        trie.deleteWord(inputWord)
        # then
        assert trie.checkIfWordExists(inputWord) is not True

    def test_deleteLongerButLeaveShorterWord(self, trie, word, words):
        # when
        trie.deleteWord("words")
        # then
        assert trie.checkIfWordExists("word") is True

    def test_autoCompletion(self, trie, word, words, wordy):
        assert trie.autoCompletion("word") == ["word", "words", "wordy"]
