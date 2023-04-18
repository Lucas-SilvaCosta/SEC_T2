import os

def getSeed(numberOfWords):
    seed = [0 for _ in range(numberOfWords)]
    for i in range(numberOfWords):
        with open('/dev/random', 'rb') as f:
            seed[i] = int.from_bytes(f.read(4), 'big')
    return seed

#print(getSeed(4))