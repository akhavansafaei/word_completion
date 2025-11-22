# Word Completion System

A Python-based word completion (autocomplete) system that implements and compares three different data structure approaches: Array-based, Linked List-based, and Trie-based dictionaries.

## Overview

This project provides a comprehensive implementation of a word frequency dictionary with autocomplete functionality. It supports multiple operations including search, add, delete, and autocomplete suggestions based on word prefixes. The system is designed to compare the performance and efficiency of different data structures for storing and retrieving word-frequency pairs.

## Features

- **Multiple Data Structure Implementations**:
  - **Array Dictionary**: Sorted array with binary search (O(log n) search)
  - **Linked List Dictionary**: Linear traversal approach (O(n) search)
  - **Trie Dictionary**: Tree-based structure optimized for prefix matching (O(m) search, where m is word length)

- **Core Operations**:
  - `Search`: Find a word and return its frequency
  - `Add`: Insert a new word with its frequency
  - `Delete`: Remove a word from the dictionary
  - `Autocomplete`: Return top 3 most frequent words matching a given prefix

## Project Structure

```
word_completion/
├── codes/
│   └── Assign1-s12345-s67890/
│       ├── dictionary/
│       │   ├── __init__.py
│       │   ├── base_dictionary.py          # Base class interface
│       │   ├── word_frequency.py           # WordFrequency data class
│       │   ├── array_dictionary.py         # Array-based implementation
│       │   ├── linkedlist_dictionary.py    # Linked list implementation
│       │   └── trie_dictionary.py          # Trie-based implementation
│       ├── dictionary_file_based.py        # Main entry point
│       ├── dictionary_test_script.py       # Automated testing script
│       ├── generation/
│       │   ├── generate.py                 # Data generation script
│       │   └── sampleData*.txt            # Various sized datasets
│       └── sampleData.txt                  # Sample word-frequency data
├── sampleDataToy.txt                       # Toy dataset for testing
├── testToy.in                              # Sample command file
├── testToy.exp                             # Expected output file
├── colab_testings.ipynb                    # Jupyter notebook for testing
└── dict.ipynb                              # Dictionary analysis notebook
```

## Installation

### Prerequisites

- Python 3.x
- No external dependencies required (uses only standard library)

### Setup

Clone the repository:
```bash
git clone <repository-url>
cd word_completion
```

## Usage

### Basic Command Line Usage

```bash
python3 codes/Assign1-s12345-s67890/dictionary_file_based.py <approach> <data_file> <command_file> <output_file>
```

**Parameters**:
- `<approach>`: Choose from `array`, `linkedlist`, or `trie`
- `<data_file>`: Path to file containing word-frequency pairs
- `<command_file>`: Path to file containing commands to execute
- `<output_file>`: Path where results will be written

### Example

```bash
python3 codes/Assign1-s12345-s67890/dictionary_file_based.py array sampleDataToy.txt testToy.in output.txt
```

### Data File Format

The data file should contain word-frequency pairs, one per line:
```
cute 10
ant 20
cut 30
cuts 50
apple 300
```

### Command File Format

The command file supports the following operations:

- `S <word>`: Search for a word
- `A <word> <frequency>`: Add a word with frequency
- `D <word>`: Delete a word
- `AC <prefix>`: Autocomplete - find top 3 words matching prefix

**Example command file**:
```
S cute
D cute
S cute
A book 10000
S book
AC c
AC cut
```

### Output Format

```
Found 'cute' with frequency 10
Delete 'cute' succeeded
NOT Found 'cute'
Add 'book' succeeded
Found 'book' with frequency 10000
Autocomplete for 'c': [ courage: 1000 cub: 15 cuts: 50 ]
Autocomplete for 'cut': [ cuts: 50 cut: 30 cute: 10 ]
```

## Testing

### Automated Testing

Run the provided test script to verify implementations:

```bash
python codes/Assign1-s12345-s67890/dictionary_test_script.py [-v] <code_directory> <implementation> <data_file> <test_files...>
```

**Example**:
```bash
python codes/Assign1-s12345-s67890/dictionary_test_script.py -v codes/Assign1-s12345-s67890 trie sampleDataToy.txt testToy.in
```

The `-v` flag enables verbose mode to show detailed test output.

### Available Test Datasets

The project includes multiple sample datasets of varying sizes for performance testing:
- `sampleData500.txt` (500 words)
- `sampleData1k.txt` (1,000 words)
- `sampleData2k.txt` (2,000 words)
- `sampleData10k.txt` (10,000 words)
- `sampleData20k.txt` (20,000 words)
- `sampleData50k.txt` (50,000 words)
- `sampleData100k.txt` (100,000 words)
- `sampleData200k.txt` (200,000 words)

## Implementation Details

### Array Dictionary
- Uses a sorted array maintained in alphabetical order
- Binary search for O(log n) lookup time
- Insertion/deletion requires shifting elements: O(n)
- Autocomplete: Linear scan for prefix matches, then sort by frequency

### Linked List Dictionary
- Simple linked list structure
- Linear search: O(n) for all operations
- Easy insertion and deletion at found position
- Autocomplete: Traverse entire list, filter by prefix, sort by frequency

### Trie Dictionary
- Tree structure where each node represents a character
- Search/insert/delete: O(m) where m is word length
- Excellent for prefix-based operations
- Autocomplete: Navigate to prefix node, then DFS to collect all words

## Performance Comparison

| Operation    | Array       | Linked List | Trie        |
|--------------|-------------|-------------|-------------|
| Search       | O(log n)    | O(n)        | O(m)        |
| Insert       | O(n)        | O(n)        | O(m)        |
| Delete       | O(n)        | O(n)        | O(m)        |
| Autocomplete | O(n log n)  | O(n log n)  | O(k)        |

where:
- n = number of words in dictionary
- m = length of the word
- k = number of words with given prefix

## Jupyter Notebooks

The project includes Jupyter notebooks for interactive analysis:
- `colab_testings.ipynb`: Comprehensive testing and benchmarking
- `dict.ipynb`: Dictionary implementation analysis

## Author

**Son Hoang Dau**
Copyright 2022, RMIT University

## License

This project is part of the Algorithms & Analysis course assignment.
