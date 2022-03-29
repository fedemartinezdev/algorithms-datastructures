def reverseDigits(number):
    digits = []
    while number > 0:
        int_part = number // 10
        decimal_part = (number / 10.0) - int_part
        digits.append(decimal_part * 10)
        number = int_part

    reverse_number = 0
    for i in range(len(digits)):
        reverse_number += digits[i] * (10 ** (len(digits) - 1 - i))

    return int(reverse_number)

print(reverseDigits(1234))