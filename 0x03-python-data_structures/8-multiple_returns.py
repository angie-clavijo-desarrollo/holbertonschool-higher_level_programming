#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence)):
        if sentence == 0:
            return None
        if sentence:
            return(len(sentence), (sentence[0]))
