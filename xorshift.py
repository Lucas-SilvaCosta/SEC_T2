from seed import getSeed
import math

# https://github.com/lucasvalentim/pequeno-teorema-de-fermat

# n is the bit size expect for the number output
def xorshift(n):
    s = getSeed(math.ceil(n/32))
    for e in range(len(s)):
        for i in range(4):
            s[e] = xorshiftRound(s[e])
    
    # Truncating last word to the right amount of bits
    diff = n % 32
    s[len(s) - 1] = s[len(s) - 1] & (pow(2, diff+1) - 1)
    
    # Concatenating words
    return concatenateWords(s)

def xorshiftGivenSeed(n, s):
    for e in range(len(s)):
        for i in range(4):
            s[e] = xorshiftRound(s[e])
    
    # Truncating last word to the right amount of bits
    diff = n % 32
    s[len(s) - 1] = s[len(s) - 1] & (pow(2, diff+1) - 1)
    
    # Concatenating words
    return concatenateWords(s)

def xorshiftInterval(min, max):
    if max - min - 1 == 0:
        return -1
    s = getSeed(math.ceil(min/32)+1)
    for e in range(len(s)):
        for i in range(4):
            s[e] = xorshiftRound(s[e])
    
    # Concatenating words
    number = concatenateWords(s) % max
    # if the function is used reasonable this shouldn't be a problem 
    if number <= min:
        number = xorshiftInterval(min, max)

    return number

def xorshiftRound(n):
    n = (n ^ (n << 13)) % pow(2, 32)
    n = (n ^ (n >> 17)) % pow(2, 32)
    n = (n ^ (n << 5)) % pow(2, 32)
    return n

def concatenateWords(w):
    number = ''
    for e in w:
        number += str(e)
    return int(number)

#print(xorshift(128))
#print(xorshiftInterval(0, 100))
