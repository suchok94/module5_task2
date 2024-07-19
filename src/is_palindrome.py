def is_palindrome(number):
    assert isinstance(number, int), TypeError('Type error')

    # number = str(number)
    # for i in range(0, len(number) // 2, 1):
    #     if number[i] != number[-i - 1]:
    #         return False
    # return True

    boof = number
    reverse_number = 0
    while boof > 0:
        reverse_number = reverse_number * 10 + boof % 10
        boof = boof // 10

    if number == reverse_number:
        return True
    else:
        return False
