#!/usr/bin/env python

import re
import sys

''' convert text file into list of words '''

def converttext(path):
    text = open(path).read()
    text = re.sub('\\n', " ", text)
    text = re.sub("\\.", " .", text)
    text = re.sub("\\!", " !", text)
    text = re.sub("\\?", " ?", text)
    text = re.sub('\\"', "", text)
    text = re.sub(" \\. . .", ".", text)
    text = text.split()
    return text

''' define wordtable function to parse text into probability table'''

def wordtable(input):
    preffix = []
    suffix = []
    for i in range(len(input)-1):
        if input[i] not in preffix:
            preffix.append(input[i])
            suffix.append([input[i+1]])
        else:
            a = preffix.index(input[i])
            suffix[a].append(input[i+1])
    d = dict(zip(preffix, suffix))
    return d
  
''' generate random markov text '''
               
def markov(dictionary, length):
    import random
    x = random.randrange(0, len(dictionary)-1)
    text = [dictionary.keys()[x]]
    for i in range(length-1):
        word = text[i]
        if len(dictionary[word]) > 1:
            y = random.randrange(0, len(dictionary[word])-1)
            text.append(dictionary[word][y])
        else:
            text.append(dictionary[word][0])
    result = ' '.join(text)   
    result = re.sub(" \\.", ".", result)
    result = re.sub(" \\!", "!", result)
    result = re.sub(" \\?", "?", result)
    return result

if __name__ == "__main__":
    args = sys.argv
    textlist = converttext(args[1])
    textdict = wordtable(textlist)
    print markov(textdict, int(args[2]))
