#!/usr/bin/env python3
# return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# squared_lc = [n ** 2 for n in range]

# make_exclamation(["Bring me a shrubbery", "We are the knights who say ni", "WHAT... is the capitol of Syria"])

def return_evens(num_list):
    even_num_list = [n for n in num_list if n % 2 ==0]
    return even_num_list

def make_exclamation(sentence_list):
    exclaimed_sentence_list = [sentence + '!' for sentence in sentence_list]
    return exclaimed_sentence_list