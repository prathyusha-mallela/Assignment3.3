# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:10:18 2017

@author: Prathyusha Mallela
"""
#Assignment longest_word 3.3
def longest_word(wordlist):
   longest=max(wordlist,key=lambda x:(len(x),x))
   #print(longest)
   return longest
    
lst=['a','ab','abc','abcd','abcde','ghyhghbibujbhjohniohniohn']
m=longest_word(lst)
print(m)
