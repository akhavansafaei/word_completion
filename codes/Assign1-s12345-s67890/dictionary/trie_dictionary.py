from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        # TO BE 
        # Initialize the root node of the Trie
        self.root = TrieNode()
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        for word_freq in words_frequencies:
            self.add_word_frequency(word_freq)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        node = self.root # Start searching from the root node
        for char in word:
            if char not in node.children: # If the current character is not found in the Trie, the word is not present.
                return 0
            node = node.children[char]
            # Check if the current node marks the end of a word; if so, return its frequency, otherwise return 0.
        return node.frequency if node.is_last else 0

        


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        node = self.root # Start from the root of the Trie
        for char in word_frequency.word:
            if char not in node.children:
                # If the current character is not in the Trie, create a new node for it.
                node.children[char] = TrieNode(letter=char)
            node = node.children[char] # Move to the child node for the current character
        if node.is_last:
            # If the node already marks the end of another word, return False (word is already in the Trie).
            return False
        node.is_last = True # Mark the current node as the end of a word
        node.frequency = word_frequency.frequency # Set the frequency of the word
        return True  # Return True to indicate successful addition of the word

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # This recursive function is responsible for deleting a word from the Trie.
        def _delete(node, word, index):
            if index == len(word):
                # If the end of the word is reached, check if the current node marks the end of a word.
                if node.is_last:
                    # If it does, mark it as not the end of a word, effectively deleting the word.
                    node.is_last = False
                    return True
                return False
            char = word[index]
            if char not in node.children:
                # If the character in the word is not found in the Trie, the word is not present for deletion.
                return False
            if _delete(node.children[char], word, index + 1):
                if not node.children[char].children and not node.children[char].is_last:
                    # If the child node has no other children and is not the end of another word, it can be safely deleted.
                    del node.children[char]
                return True
            return False
        # Call the _delete function starting from the root node and index 0 (beginning of the word).
        return _delete(self.root, word, 0)


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        def _find_words_with_prefix(node, prefix, word_list):
            if node.is_last:
                # If the current node marks the end of a word, add it to the word list.
                word_list.append((prefix, node.frequency))
            for char, child_node in node.children.items():
                 # Recursively explore child nodes with the updated prefix.
                _find_words_with_prefix(child_node, prefix + char, word_list)

        node = self.root
        for char in word:
            if char not in node.children:
                # If a character in the input word is not found in the Trie, return an empty list.
                return []
            node = node.children[char]

        word_list = []
        _find_words_with_prefix(node, word, word_list)
        word_list.sort(key=lambda x: x[1], reverse=True)
        # Return the top 3 words with the highest frequencies as WordFrequency objects.
        return [WordFrequency(word, freq) for word, freq in word_list[:3]]
