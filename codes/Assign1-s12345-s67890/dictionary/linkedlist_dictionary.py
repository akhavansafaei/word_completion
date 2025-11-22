from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.head = None


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        #words_frequencies.sort(key=lambda x: x.frequency, reverse=True)

        # Create nodes and build the linked list
        for word_frequency in words_frequencies:
            self.add_word_frequency(word_frequency)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        # TO BE IMPLEMENTED
        current = self.head
        while current:
            if current.word_frequency.word == word:
                return current.word_frequency.frequency
            current = current.next
        return 0
        

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # TO BE IMPLEMENTED
        new_node = ListNode(word_frequency)

        # If the linked list is empty, insert the new node as the head
        if not self.head:
            self.head = new_node
            return True

        # Traverse the linked list to check for duplicates
        current = self.head
        prev = None
        while current:
            if current.word_frequency.word == word_frequency.word:
                return False  # Word is already in the dictionary
            prev = current
            current = current.next

        # Insert the new node at the end of the linked list
        prev.next = new_node
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        # TO BE IMPLEMENTED
        current = self.head
        prev = None
        while current:
            if current.word_frequency.word == word:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # TO BE IMPLEMENTED
        autocomplete_results = []

        current = self.head
        
        while current:
            if current.word_frequency.word.startswith(word):
                autocomplete_results.append(current.word_frequency)
                # Break when we have found 3 matching words
                
            current = current.next
            if current==self.head:
                break
        # Sort the results by frequency in descending order
        autocomplete_results.sort(key=lambda x: x.frequency, reverse=True)

        return autocomplete_results[:3]



