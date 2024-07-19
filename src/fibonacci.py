def fibonacci(number: int):
    assert isinstance(number, int), TypeError('Неправильный формат')
    list_fibonacci = [0]
    if number == 0:
        return list_fibonacci
    elif number > 0:
        list_fibonacci.append(1)
        for i in range(0, number-1, 1):
            list_fibonacci.append(list_fibonacci[i] + list_fibonacci[-1])
        return list_fibonacci
    else:
        raise ValueError("Неправильное значение")
