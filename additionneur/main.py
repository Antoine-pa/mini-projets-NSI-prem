from algebre_bool import table3
from dec_to_bin import dec_bin
from bin_to_dec import bin_dec

def additionneur_1_bit(a, b, c):
    somme = c ^ (a ^ b)
    reste = a and b or c and (a ^ b)
    return somme, reste


def additionneur_complet(n1, n2):
    n1 = dec_bin(n1)[:-2][::-1]
    n2 = dec_bin(n2)[:-2][::-1]

    if len(n1) > len(n2):
        n2 += ["0" for _ in range(len(n1)-len(n2))]
    else:
        n1 += ["0" for _ in range(len(n2)-len(n1))]
    c = 0
    result = []
    for i in range(len(n1)):
        a = int(n1[i])
        b = int(n2[i])
        add = additionneur_1_bit(a, b, c)
        result.append(str(add[0]))
        c = int(add[1])
    if c == 1:
        result.append(str(c))
        n1.append("0")
        n2.append("0")
    print("".join(n1[::-1]), bin_dec("".join(n1[::-1])))
    print("".join(n2[::-1]), bin_dec("".join(n2[::-1])))
    print("".join(result[::-1]), bin_dec("".join(result[::-1])))
    print("--------")
    return result[::-1]

def multiplicateur(n1, n2):
    _out = 0
    for a in range(n2):
        _out = bin_dec("".join(additionneur(_out, n1)))
    print("résultat :", _out)
    return 0

multiplicateur(3, 6)
