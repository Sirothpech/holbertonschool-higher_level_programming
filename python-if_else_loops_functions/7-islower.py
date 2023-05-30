#!/usr/bin/pyhton3
def islower(c):
    if ord(c) in range(ord('a'), ord('z')+1):
        return True
    elif ord(c) in range(ord('A'), ord('Z')+1):
        return False
    else:
        return False
