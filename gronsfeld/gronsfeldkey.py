'''
Created on 4 sept. 2017

@author: sfonteneau
'''

class GronsfeldKey:
    
    def __init__(self, rawkey):
        K = map(lambda c: int(c), rawkey)
        self.value= list(K)