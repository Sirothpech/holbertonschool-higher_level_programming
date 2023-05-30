#!/usr/bin/pyhton3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    elif ord(c) in range(65, 91):
        return False
    else:
        return False
