from seed import getSeed
import math

# Reference for the algorithm:
#   https://eprint.iacr.org/2006/438.pdf
#   https://realpython.com/python-bitwise-operators/
#   https://en.wikipedia.org/wiki/ISAAC_(cipher)
# Isaac é um PRNG que gera números com 32-bits. No desenvolvimento pensei na possibilidade de implementar
# um Isaac com 8-bits, mas as acabariam impactando mais o algoritmo que o esperado. Por exemplo, o número
# de shifts da função f teriam de ser alterados e não tenho certeza se os valores são arbitrários ou são
# aqueles por um motivo. Por isso decide manter o algoritmo com palavras de 32-bits, apenas alterando o
# número de palavras a serem geradas de acordo com o tamanho do número esperado.


# 's' (BitVector, size = n)is the secret initial state or seed
# 'n' (Integer) is the the bit size the algorithm should run in
def isaac(n):
    s = getSeed(math.ceil(n/32))
    # a is used as an entropy accumulator
    a = 0
    # b contains the previous pseudo-random word
    b = 0
    # c is a simple counter, incremented at each round of the algorithm.
    c = 0
    # nw is the number of 32-bit words needed to make a n-bit number
    nw = math.ceil(n/32)
    w = isaacRound(s, nw, a, b, c)

    # Truncating last word to the right amount of bits
    diff = n % 32
    w[len(w) - 1] = w[len(w) - 1] & (pow(2, diff+1) - 1)

    return concatenateWords(w)

def isaacGivenSeed(n, s):
    # a is used as an entropy accumulator
    a = 0
    # b contains the previous pseudo-random word
    b = 0
    # c is a simple counter, incremented at each round of the algorithm.
    c = 0
    # nw is the number of 32-bit words needed to make a n-bit number
    nw = math.ceil(n/32)
    w = isaacRound(s, nw, a, b, c)

    # Truncating last word to the right amount of bits
    diff = n % 32
    w[len(w) - 1] = w[len(w) - 1] & (pow(2, diff+1) - 1)

    return concatenateWords(w)
    
def isaacInterval(min, max):
    if max - min - 1 == 0:
        return -1
    
    s = getSeed(math.ceil(min/32)+1)
    a = 0
    b = 0
    c = 0
    nw = math.ceil(min/32+1)
    w = isaacRound(s, nw, a, b, c)

    # Concatenating words
    number = concatenateWords(w) % max
    # if the function is used reasonable this shouldn't be a problem 
    if number <= min:
        s = getSeed(math.ceil(min/32)+1)
        a = 0
        b = 0
        c = 0
        nw = math.ceil(min/32+1)
        number = concatenate(isaacRound(s, nw, a, b, c)) % max

    return number

def isaacRound(s, n, a, b, c):
    c += 1
    b += c
    r = [0 for _ in range(n)]
    for i in range(n):
        x = s[i]
        a = (f(a, i) + s[(i+math.floor(n/2)) % n])  % pow(2, 32)
        s[i] = (a + b + s[(x >> 2) % n]) % pow(2, 32)
        r[i] = (x + s[(s[i] >> 10) % n])  % pow(2, 32)
        b = r[i]
    if c < n:
        r = isaacRound(r, n, a, b, c)
    return r

def f(a, i):
    m = i % 4
    if (m == 0):
        return a << 13
    elif (m == 1):
        return a >> 6
    elif (m == 2):
        return a << 2
    return a >> 16
    
def concatenateWords(w):
    number = ''
    for e in w:
        number += str(e)
    return int(number)

#print(isaac(128))
#print(isaacInterval(0, 100))
