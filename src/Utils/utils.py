def decimal_to_q_ary(num, base, length=0):
    remainder_stack = []

    while num > 0:
        remainder = num % base
        remainder_stack.append(str(remainder))
        num = num // base

    base_ary_digits = remainder_stack[::-1]

    zeros = []
    if length > len(base_ary_digits):
        zeros = ['0' for i in range(0, length - len(base_ary_digits))]    
    return ''.join(zeros + base_ary_digits)

def find_max_idxs(l: list):
    maximum = max(l)
    return [i for i, j in enumerate(l) if j == maximum]
