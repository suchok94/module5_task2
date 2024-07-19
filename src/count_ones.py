def count_ones(number: int):
    assert isinstance(number, int), TypeError("Неправильный формат")
    if number >= 0:
        count = 0
        while number:
            if number % 2 == 1:
                count += 1
                number = number // 2
            else:
                number //= 2
    else:
        raise ValueError("Неправильное число")
    return count

