'''
Created on 3 sept. 2017

@author: sfonteneau
'''
from . import textutils

def decipher(ciphertext, key):
    result = list()
    for i in range(0, len(ciphertext)):
        letter = ciphertext[i]
        deciphered_letter = textutils.rotate(letter, -key.value[i%len(key.value)])
        result.append(deciphered_letter)
    return ''.join(result)
