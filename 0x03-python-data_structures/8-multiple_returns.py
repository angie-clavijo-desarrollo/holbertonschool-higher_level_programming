#!/usr/bin/python3
def multiple_returns(sentence):
    size = (len(sentence))
    if (sentence):
        first_letter = sentence[0]
        return(size, first_letter)
    return(size, None)
