def image_inverse(value):
    return 1/value

def maximum(val1, val2):
    im1, im2 = image_inverse(val1), image_inverse(val2)
    if im1 > im2:
        op = ">"
    elif im1 < im2:
        op = "<"
    else:
        op = "="

    return f"(f({val1}) = {im1}) {op} (f({val2}) = {im2})"


def prix(nb_photo):
    if nb_photo > 50:
        p = 50*0.17 + (nb_photo-50)*0.16
        if nb_photo > 100:
            return p * 0.9
        return p
    else:
        return nb_photo*0.17
