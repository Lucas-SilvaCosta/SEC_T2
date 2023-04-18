import math
from decimal import Decimal, getcontext
getcontext().prec = 2000

from isaac import isaacInterval
from xorshift import xorshiftInterval

# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# Material da aula

def rewrite(n):
    k = 0
    kf = 0
    m = n - 1
    mf = 0
    while m % 2 == 0:
        m = Decimal(m)/Decimal(2)
        k = k + 1
    return k, int(m)

def millerRabinIsaac(n):
    k, m = rewrite(n)
    a = isaacInterval(1, n-1)
    b = pow(a, m, n)
    if b % n == 1:
        return True
    for i in range(k-1):
        if (b+1) % n == 0:
            return True
        else:
            b = pow(b, 2, n)
    return False

def millerRabinXorshift(n):
    k, m = rewrite(n)
    a = xorshiftInterval(1, n-1)
    b = pow(a, m, n)
    if b % n == 1:
        return True
    for i in range(k-1):
        if (b+1) % n == 0:
            return True
        else:
            b = pow(b, 2, n)
    return False

#print(millerRabinIsaac(6700417))
#print(millerRabinXorshift(6700417))

#print(rewrite(6700417))