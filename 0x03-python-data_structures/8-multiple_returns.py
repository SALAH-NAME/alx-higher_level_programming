#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (None, None)
    else:
        return (len(sentence), sentence[0])
