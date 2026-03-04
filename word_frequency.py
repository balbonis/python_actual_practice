# This program counts the frequency of each word in a given sentence. It uses the Counter class from the collections module to count the occurrences of each word and then prints the unique words along with their corresponding counts.
# Example:
# Input: "hello world hello"
# Output: "['hello', 'world']   [2, 1]"         
# Achievement: This program effectively demonstrates the use of the Counter class to analyze word frequency in a sentence, showcasing the ability to manipulate and count elements in a list.
# The program takes a sentence as input, splits it into words, and then uses Counter to count how many times each word appears. Finally, it prints the list of unique words and their respective counts.
# use Counter to count the frequency of each word in the input sentence. The Counter class takes an iterable (in this case, the list of words obtained by splitting the input text) and returns a dictionary-like object where the keys are the unique words and the values are their corresponding counts. The program then prints the list of unique words (keys) and their counts (values) separately.
# keys() method is used to retrieve the unique words from the Counter object, and values() method is used to retrieve the counts of each word. The output displays the unique words and their frequencies in a clear format.

from collections import Counter
text = input ("Enter sentence: ")

counts = Counter(text.split())

print (list(counts.keys()), " " , list(counts.values()))

