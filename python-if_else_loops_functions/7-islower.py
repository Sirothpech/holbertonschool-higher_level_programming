#!/usr/bin/pyhton3
def islower(c):
    if ord(c) in range(97, 122):
        return True
    elif ord(c) in range(65, 90):
        return False
