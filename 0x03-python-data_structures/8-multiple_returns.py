#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) > 0):
        if sentence:
            return(len(sentence), (sentence[0]))
    else:
        return None
