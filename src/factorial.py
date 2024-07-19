def factorial(number: int):
    factorial = 1
    if number == 0:
        factorial = 1
    elif number > 0 and number <= 20:
        for i in range(1, number + 1):
            factorial = factorial * i
    else:
        raise ValueError("Неправильное значение")
    return factorial


