def digits_sum(sum):
    sum_digits = 0

    while sum != 0:
        digit = sum % 10
        sum //= 10
        sum_digits += digit
    return sum_digits
