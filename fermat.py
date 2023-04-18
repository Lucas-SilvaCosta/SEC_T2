from isaac import isaacInterval
from xorshift import xorshiftInterval

# https://pt.wikipedia.org/wiki/Teste_de_primalidade_de_Fermat
# https://github.com/lucasvalentim/pequeno-teorema-de-fermat

def fermatIsaac(n):
    if n <= 1 or n == 4:
        return False
    elif n <= 3:
        return True
    else:
        for i in range(20):
            a = isaacInterval(1, n-1)
            if pow(a, n-1, n) != 1:
                return False
        return True

def fermatXorshift(n):
    if n <= 1 or n == 4:
        return False
    elif n <= 3:
        return True
    else:
        for i in range(20):
            a = xorshiftInterval(2, n-2)
            if pow(a, n-1, n) != 1:
                return False
        return True

#print(fermatIsaac(6700417))
#print(fermatXorshift(6700417))