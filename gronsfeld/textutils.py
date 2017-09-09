'''
Created on 4 sept. 2017

@author: sfonteneau
'''
from string import lowercase

def rotate(character, offset):
    i = lowercase.index(character)
    return lowercase[(i + offset) % 26]

def score(message, expected_words):
    score = 0
    
    offsets = dict()
    for word in expected_words:
        offsets[word] = 0
    
    for c in message:
        for word in expected_words:
            if c == word[offsets[word]]:
                offsets[word] += 1
                score += offsets[word]
                offsets[word] %= len(word)
            elif offsets[word] != 0:
                offsets[word] = 0

    return score