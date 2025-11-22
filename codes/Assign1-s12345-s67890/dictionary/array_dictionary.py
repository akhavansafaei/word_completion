from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.word_frequencies = []
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

        # Use binary search to find the word
        idx = bisect.bisect_left([wf.word for wf in self.word_frequencies], word)
        if idx < len(self.word_frequencies) and self.word_frequencies[idx].word == word:
            return self.word_frequencies[idx].frequency
        else:
            return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        idx = bisect.bisect_left([wf.word for wf in self.word_frequencies], word_frequency.word)

        # Check if the word is already in the dictionary
        if idx < len(self.word_frequencies) and self.word_frequencies[idx].word == word_frequency.word:
            return False
        else:
            # Insert the new word frequency at the correct position to maintain the sorted order
            self.word_frequencies.insert(idx, word_frequency)
            return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        # TO BE IMPLEMENTED
        # Use binary search to find the word's index
        idx = bisect.bisect_left([wf.word for wf in self.word_frequencies], word)

        # Check if the word is found in the dictionary
        if idx < len(self.word_frequencies) and self.word_frequencies[idx].word == word:
            # Remove the word frequency from the list
            del self.word_frequencies[idx]
            return True
        else:
            return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # TO BE IMPLEMENTED
        # Initialize a list to store autocomplete results
        autocomplete_results = []

        # Iterate through the sorted list of word frequencies
        for word_frequency in self.word_frequencies:
            if word_frequency.word.startswith(prefix_word):
                autocomplete_results.append(word_frequency)

        # Sort the results in descending order based on frequency
        autocomplete_results.sort(key=lambda x: x.frequency, reverse=True)

        # Return only the top 3 results or fewer if there are less than 3 results
        return autocomplete_results[:3]
