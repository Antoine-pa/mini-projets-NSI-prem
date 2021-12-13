def dec_bin(num: float) -> list:
    if num == 0:
        return ["0"]
    mantisse = []
    int_num = int(num)
    num -= int_num
    while int_num not in (0, 1):
        mantisse.append(str(int_num % 2))
        int_num //= 2
    mantisse.append(str(int_num))
    mantisse = mantisse[::-1]

    if num != 0:
        mantisse.append(".")
        for a in range(23):
            num *= 2
            if num >= 1:
                num -= 1
                mantisse.append("1")
            else:
                mantisse.append("0")
    else:
        mantisse += [".", "0"]

    return mantisse


def exposant_mantisse(num: float) -> list:
    mantisse = bin(num)
    if "1" not in mantisse:
        mantisse = "00000000000000000000000"
        exposant = "11111111"
        return exposant, mantisse
    mantisse = float("".join(mantisse))
    exposant = 0
    if mantisse < 1:
        while mantisse < 1:
            mantisse *= 10
            exposant -= 1
    else:
        while mantisse > 2:
            mantisse /= 10
            exposant += 1
    mantisse = str(mantisse)[2:]
    mantisse += "".join(["0" for a in range(23-len(mantisse))])
    return exposant_bin(exposant), mantisse

def exposant_bin(exposant: int) -> int:
    exposant += 127
    exposant = ("".join(bin(exposant)))[:-2]
    return "".join(["0" for a in range(8-len(exposant))]) + exposant

def norme_IEEE(n: float) -> int:
    signe = str(int(n < 0))
    return signe + "".join(exposant_mantisse(n))

def somme_float_bin_IEEE(m, n):
    result = m + n
    return norme_IEEE(result)

def norme_IEEE(n: float) -> int:
    signe = str(int(n < 0))
    return signe + "".join(exposant_mantisse(n))
