'''
A python program to count the 25 most common words appearing in pride and prejudice
Nate Weeks April 2018
'''

import string
from collections import Counter

#method read from a file and to create the array of words to be ignored
def createStopArray():
    with open("stop-words.txt") as f:
        for line in f:
            splitLine = line.split(",") #splitting each word into a seperate array entry
        stopArray = splitLine[:-1]      # ignore the extra space at the end
    return stopArray

# method to read from a file and remove all punctuation and format the text of pride and prejudice into an array of strings
def formatContent():
    formattedContent = []   # intiate the array
    with open("pride-and-prejudice.txt") as f:
        for line in f:
            # function to remove the punctuation, turn everything to lowercase, then split the words into an array of strings
            formattedContent += ((line.translate(None, string.punctuation)).lower()).split()
    return formattedContent

# takes an array of content and an array of words to ignore and outputs the 25 most common words and how often they occur
def countWords(formatted_content, stop_words):
    word_array = []         # initiate the array
    for word in formatted_content:
        if word not in stop_words:      # check to see if the word is in stop_words
            word_array.append(word)     # if its not, add it to the word array
    counter = Counter(word_array)       # input the word_array into a counter dictionary
    return counter.most_common(25)      # return the 25 most common words and their number of occurences

# takes a counter object and outputs a string formatted as requested
def formatCount(counter):
    for item in counter:
        print item[0] + " - " + str(item[1])

# driver function that calls and chains each function together
def main():
    formatted_content = formatContent()
    stop_words = createStopArray()
    counter = countWords(formatted_content, stop_words)
    print "The most common words in pride and prejudice not included in the stop words are:"
    formatCount(counter)

main()
