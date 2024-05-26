#!/usr/bin/python3
def multiple_returns(phrase):
    if not phrase:
        return (0, None)
    else:
        return (len(phrase), phrase[0])
