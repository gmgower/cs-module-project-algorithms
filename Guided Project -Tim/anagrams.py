
# given a file of words, find the largest set of anagrams

# Understand
## what the heck is an anagram?
## how do we get the words? file, format

# i am lord voldemort == tom marvolo riddle
# bat, tab
# dad, add

# what is a set?
## the group of all words that are anagrams of each other

# we are going to find all groups of anagrams and return the largest set

# Plan
## same number of letters
## should be equal when sorted
## how to handle case? lowercase or uppercase everything. lowercase

# Scoring approach
## assign each letter of the alphabet a unique value
# make a dictionary for #{word_score: [word1, word2, word3],
#                         word_score2: [word1, word2]
#                        }

## for every word
### calculate the word's unique score
#### for every letter, look up its unique random value
#### add them together to make the unique score/signature
### add the word to the dictionary

## find the largest set in the dictionary

## return the largest set


# Sorting approach?

# collections.Counter?


# Execute
import random
import sys

def find_anagrams(words):
## assign each letter of the alphabet a unique value
    chars = [0] * 26
    for i in range(26):
        chars[i] = random.randint(0, 1000000)
        
# make a dictionary for #{word_score: [word1, word2, word3],
#                         word_score2: [word1, word2]
#                        }
    anagram_sets = {}

## for every word
    for word in words:
        word = word.lower()
### calculate the word's unique score
        word_score = 0
#### for every letter, look up its unique random value
        for letter in word:
            index = ord(letter) - 97
            #### add them together to make the unique score/signature
            try:
                word_score += chars[index]
            except IndexError:
                print(letter)
                continue
                # sys.exit(1)

            
### add the word to the dictionary
        if word_score not in anagram_sets:
            anagram_sets[word_score] = []
        anagram_sets[word_score].append(word)

## find the largest set in the dictionary
## traverse and have a flag, and compare length
    longest_set_length = 0
    longest_set_key = 0

    for key in anagram_sets:
        if len(anagram_sets[key]) > longest_set_length:
            longest_set_length = len(anagram_sets[key])
            longest_set_key = key

## return the largest set
    return anagram_sets[longest_set_key]

file = open('words.txt', 'r')
words = file.read().split("\n")
file.close()

print(find_anagrams(words))


# Review
## Create a helper function to calculate the word score recursively
## Plan didn't include non-alphabetic characters